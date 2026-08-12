#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["tqdm>=4.66,<5"]
# ///
"""Mirror selected LangChain documentation sections as Markdown.

Discovery uses the site's sitemap, llms.txt, the configured entry points, and
links found in downloaded Markdown. Files are written atomically, and only
files recorded in the previous managed manifest are eligible for stale-file
cleanup.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import re
import shutil
import sys
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urljoin, urlsplit, urlunsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

try:
    from tqdm import tqdm
except ImportError as exc:  # pragma: no cover - depends on the local environment
    uv = shutil.which("uv")
    if uv:
        os.execv(uv, [uv, "run", "--script", str(Path(__file__).resolve()), *sys.argv[1:]])
    raise SystemExit(
        "Missing dependency: install it with `python3 -m pip install tqdm`, "
        "or install uv so this script can provision tqdm automatically."
    ) from exc


ORIGIN = "https://docs.langchain.com"
SITEMAP_URL = f"{ORIGIN}/sitemap.xml"
LLMS_URL = f"{ORIGIN}/llms.txt"
OUTPUT_ROOT = Path(__file__).resolve().parent
MANIFEST_PATH = OUTPUT_ROOT / ".mirror-manifest.json"
USER_AGENT = "langchain-docs-markdown-mirror/1.0"


@dataclass(frozen=True)
class Section:
    folder: str
    prefix: str
    entry_url: str | None
    local_subfolder: str = ""
    root_relative: str = "index"


SECTIONS = (
    Section(
        "deepagents",
        "/oss/deepagents",
        f"{ORIGIN}/oss/deepagents/",
        root_relative="code/index",
    ),
    Section("deepagents", "/oss/python/deepagents", f"{ORIGIN}/oss/python/deepagents/"),
    Section("langchain", "/oss/python/langchain", f"{ORIGIN}/oss/python/langchain/"),
    Section("langgraph", "/oss/python/langgraph", f"{ORIGIN}/oss/python/langgraph/"),
    Section("OpenWiki", "/oss/openwiki", f"{ORIGIN}/oss/openwiki/"),
    Section("integrations", "/oss/python/integrations", f"{ORIGIN}/oss/python/integrations/"),
    Section("langsmith", "/langsmith", f"{ORIGIN}/langsmith/"),
    # This user-requested route does not exist as of the latest run. Keeping
    # it as a discovery scope means sitemap/llms pages will mirror if LangChain
    # publishes the section later, without making today's run fail on its 404.
    Section("langsmith", "/oss/python/langsmith", None, local_subfolder="oss-python"),
    # Catch-all for the complete Python documentation namespace. Keep this
    # after the explicit scopes so their established destination paths win;
    # every other current or future /oss/python/<category>/... URL is mapped
    # directly to <category>/... beneath OUTPUT_ROOT.
    Section("", "/oss/python", f"{ORIGIN}/oss/python/"),
)

URL_RE = re.compile(r"https://docs\.langchain\.com/[^\s<>\]\[()\"']+")
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+[\"'][^)]*[\"'])?\)")
HTML_LINK_RE = re.compile(r"(?:href|src)=[\"']([^\"']+)[\"']", re.IGNORECASE)
SKIP_SUFFIXES = {
    ".7z", ".avif", ".bmp", ".css", ".csv", ".doc", ".docx", ".gif",
    ".gz", ".ico", ".jpeg", ".jpg", ".js", ".json", ".map", ".mov",
    ".mp3", ".mp4", ".pdf", ".png", ".py", ".svg", ".tar", ".toml",
    ".ts", ".tsx", ".txt", ".wav", ".webm", ".webp", ".xml", ".yaml",
    ".yml", ".zip",
}


@dataclass
class Download:
    page_url: str
    final_url: str | None = None
    body: bytes | None = None
    error: str | None = None
    skipped: str | None = None


class ExternalRedirect(RuntimeError):
    def __init__(self, url: str):
        super().__init__(url)
        self.url = url


class DocsRedirectHandler(HTTPRedirectHandler):
    """Follow documentation redirects but stop before requesting other sites."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: ANN001
        absolute = urljoin(req.full_url, newurl)
        if urlsplit(absolute).netloc.lower() != "docs.langchain.com":
            raise ExternalRedirect(absolute)
        return super().redirect_request(req, fp, code, msg, headers, absolute)


OPENER = build_opener(DocsRedirectHandler())


def request_bytes(url: str, timeout: float, retries: int = 3) -> tuple[bytes, str, str]:
    """Return response body, final URL, and content type with bounded retries."""
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/markdown,text/plain,*/*"})
            with OPENER.open(req, timeout=timeout) as response:
                return response.read(), response.geturl(), response.headers.get_content_type()
        except (HTTPError, URLError, TimeoutError, OSError) as exc:
            last_error = exc
            if isinstance(exc, HTTPError) and exc.code in {400, 401, 403, 404, 410}:
                break
            if attempt + 1 < retries:
                time.sleep(0.5 * (2**attempt))
    raise RuntimeError(str(last_error) if last_error else f"Unable to fetch {url}")


def canonical_page_url(raw_url: str, base_url: str = ORIGIN) -> str | None:
    """Normalize a URL and return it only when it belongs to a configured scope."""
    raw_url = raw_url.strip().strip("<>")
    if not raw_url or raw_url.startswith(("#", "mailto:", "tel:", "data:", "javascript:")):
        return None
    absolute = urljoin(base_url, raw_url)
    parts = urlsplit(absolute)
    if parts.scheme not in {"http", "https"} or parts.netloc.lower() != "docs.langchain.com":
        return None
    path = unquote(parts.path)
    if path.endswith(".md"):
        path = path[:-3]
    path = "/" + str(PurePosixPath(path)).lstrip("/")
    if path != "/":
        path = path.rstrip("/")
    if Path(path).suffix.lower() in SKIP_SUFFIXES:
        return None
    # Template expressions and punctuation copied from code samples are not
    # documentation routes, even when a Markdown parser sees them as links.
    if any(character in path for character in '{}*"<>') or path.count("(") != path.count(")"):
        return None
    for section in SECTIONS:
        if path == section.prefix or path.startswith(section.prefix + "/"):
            return urlunsplit(("https", "docs.langchain.com", path, "", ""))
    return None


def section_for(page_url: str) -> Section:
    path = urlsplit(page_url).path
    for section in SECTIONS:
        if path == section.prefix or path.startswith(section.prefix + "/"):
            return section
    raise ValueError(f"URL is outside configured sections: {page_url}")


def local_path_for(page_url: str) -> Path:
    section = section_for(page_url)
    path = urlsplit(page_url).path
    relative = path[len(section.prefix):].strip("/")
    if not relative:
        relative = section.root_relative
    safe_parts = []
    for part in PurePosixPath(relative).parts:
        if part in {"", ".", ".."}:
            raise ValueError(f"Unsafe page path: {page_url}")
        safe_parts.append(part)
    target = OUTPUT_ROOT / section.folder
    if section.local_subfolder:
        target /= section.local_subfolder
    target /= Path(*safe_parts)
    return target.with_name(target.name + ".md")


def markdown_url(page_url: str) -> str:
    return page_url.rstrip("/") + ".md"


def discover_seed_urls(timeout: float) -> tuple[set[str], list[str]]:
    pages = {
        canonical_page_url(section.entry_url)
        for section in SECTIONS
        if section.entry_url is not None
    }
    errors: list[str] = []

    try:
        sitemap, _, _ = request_bytes(SITEMAP_URL, timeout)
        root = ET.fromstring(sitemap)
        for element in root.iter():
            if element.tag.endswith("loc") and element.text:
                page = canonical_page_url(element.text)
                if page:
                    pages.add(page)
    except Exception as exc:  # Continue with the other independent indexes.
        errors.append(f"sitemap discovery: {exc}")

    try:
        llms, _, _ = request_bytes(LLMS_URL, timeout)
        for raw_url in URL_RE.findall(llms.decode("utf-8", errors="replace")):
            page = canonical_page_url(raw_url.rstrip(".,:;"))
            if page:
                pages.add(page)
    except Exception as exc:
        errors.append(f"llms.txt discovery: {exc}")

    return {page for page in pages if page}, errors


def download_one(page_url: str, timeout: float) -> Download:
    try:
        body, final_url, content_type = request_bytes(markdown_url(page_url), timeout)
        if urlsplit(final_url).netloc.lower() != "docs.langchain.com":
            return Download(page_url=page_url, final_url=final_url, skipped="redirects outside docs.langchain.com")
        prefix = body[:200].lstrip().lower()
        if content_type == "text/html" or prefix.startswith((b"<!doctype html", b"<html")):
            raise RuntimeError("server returned HTML instead of Markdown")
        body.decode("utf-8")
        return Download(page_url=page_url, final_url=final_url, body=body)
    except ExternalRedirect as exc:
        return Download(page_url=page_url, final_url=exc.url, skipped="redirects outside docs.langchain.com")
    except (RuntimeError, UnicodeDecodeError) as exc:
        return Download(page_url=page_url, error=str(exc))


def links_from(download: Download) -> set[str]:
    if download.body is None:
        return set()
    text = download.body.decode("utf-8")
    final_page = (download.final_url or download.page_url).removesuffix(".md")
    candidates: Iterable[str] = (
        list(MARKDOWN_LINK_RE.findall(text))
        + list(HTML_LINK_RE.findall(text))
        + list(URL_RE.findall(text))
    )
    found = set()
    for candidate in candidates:
        page = canonical_page_url(candidate, final_page)
        if page:
            found.add(page)
    return found


def atomic_write(path: Path, body: bytes) -> bool:
    """Write when changed and return whether file contents were updated."""
    if path.exists() and path.read_bytes() == body:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    temporary.write_bytes(body)
    os.replace(temporary, path)
    return True


def load_previous_manifest() -> dict:
    try:
        data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return {}


def relative_output_path(path: Path) -> str:
    return path.relative_to(OUTPUT_ROOT).as_posix()


def clean_stale_files(previous: dict, current_files: set[str]) -> list[str]:
    removed: list[str] = []
    directories_to_check: set[Path] = set()
    old_files = previous.get("files", {})
    if not isinstance(old_files, dict):
        return removed
    root = OUTPUT_ROOT.resolve()
    for relative in sorted(set(old_files) - current_files):
        candidate = (OUTPUT_ROOT / relative).resolve()
        try:
            candidate.relative_to(root)
        except ValueError:
            continue
        if candidate.suffix == ".md" and candidate.is_file():
            candidate.unlink()
            removed.append(relative)
            parent = candidate.parent
            while parent != root:
                directories_to_check.add(parent)
                parent = parent.parent
    protected_directories = set()
    for section in SECTIONS:
        directory = OUTPUT_ROOT / section.folder
        if section.local_subfolder:
            directory /= section.local_subfolder
        protected_directories.add(directory.resolve())
    # Only consider directories made empty by the managed files removed above.
    # Never walk unrelated repository state such as .git or .github.
    for directory in sorted(directories_to_check, key=lambda path: len(path.parts), reverse=True):
        if directory.resolve() in protected_directories:
            continue
        try:
            directory.rmdir()
        except OSError:
            pass
    return removed


def mirror(*, workers: int, timeout: float, clean: bool) -> int:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    for section in SECTIONS:
        directory = OUTPUT_ROOT / section.folder
        if section.local_subfolder:
            directory /= section.local_subfolder
        directory.mkdir(parents=True, exist_ok=True)

    seeds, discovery_errors = discover_seed_urls(timeout)
    if not seeds:
        print("No documentation pages were discovered; existing files were left untouched.", file=sys.stderr)
        for error in discovery_errors:
            print(f"  {error}", file=sys.stderr)
        return 1

    queued = set(seeds)
    completed: dict[str, Download] = {}
    failures: dict[str, str] = {}
    broken_links: dict[str, str] = {}
    skipped: dict[str, str] = {}
    changed = 0

    with tqdm(desc="Downloading Markdown", unit="page", total=len(queued), dynamic_ncols=True) as progress:
        while True:
            batch = sorted(queued - completed.keys() - failures.keys() - broken_links.keys() - skipped.keys())
            if not batch:
                break
            with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
                futures = {executor.submit(download_one, page, timeout): page for page in batch}
                for future in concurrent.futures.as_completed(futures):
                    result = future.result()
                    if result.skipped:
                        skipped[result.page_url] = f"{result.skipped}: {result.final_url}"
                    elif result.error:
                        target = failures if result.page_url in seeds else broken_links
                        target[result.page_url] = result.error
                    else:
                        completed[result.page_url] = result
                        if atomic_write(local_path_for(result.page_url), result.body or b""):
                            changed += 1
                        new_links = links_from(result) - queued
                        if new_links:
                            queued.update(new_links)
                            progress.total = len(queued)
                            progress.refresh()
                    progress.update(1)

    files: dict[str, dict[str, str | int]] = {}
    for page_url, result in sorted(completed.items()):
        path = local_path_for(page_url)
        body = result.body or b""
        files[relative_output_path(path)] = {
            "source": page_url,
            "resolved_markdown": result.final_url or markdown_url(page_url),
            "bytes": len(body),
            "sha256": hashlib.sha256(body).hexdigest(),
        }

    previous = load_previous_manifest()
    removed = clean_stale_files(previous, set(files)) if clean and not failures else []
    manifest = {
        "schema_version": 1,
        "source": ORIGIN,
        "page_count": len(files),
        "files": files,
        "failures": failures,
        "broken_or_non_page_links": broken_links,
        "external_redirects": skipped,
        "configured_unpublished_scopes": [
            f"{ORIGIN}{section.prefix}"
            for section in SECTIONS
            if section.entry_url is None
        ],
        "discovery_warnings": discovery_errors,
    }
    atomic_write(MANIFEST_PATH, (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode())

    section_counts = {section.prefix: 0 for section in SECTIONS}
    for page in completed:
        section_counts[section_for(page).prefix] += 1
    print(f"Mirrored {len(files)} pages ({changed} changed, {len(removed)} stale removed).")
    print("Scopes: " + ", ".join(f"{name}={count}" for name, count in section_counts.items()))
    if discovery_errors:
        print("Discovery warnings:", file=sys.stderr)
        for error in discovery_errors:
            print(f"  - {error}", file=sys.stderr)
    if failures:
        print(f"Failed pages ({len(failures)}):", file=sys.stderr)
        for url, error in sorted(failures.items()):
            print(f"  - {url}: {error}", file=sys.stderr)
        print("Stale cleanup was skipped because the mirror was incomplete.", file=sys.stderr)
        return 1
    if broken_links:
        print(f"Ignored {len(broken_links)} broken/non-page links found inside documents.", file=sys.stderr)
    if skipped:
        print(f"Ignored {len(skipped)} routes that redirect outside docs.langchain.com.", file=sys.stderr)
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=12, help="parallel downloads (default: 12)")
    parser.add_argument("--timeout", type=float, default=30.0, help="per-request timeout in seconds")
    parser.add_argument("--no-clean", action="store_true", help="keep previously managed pages removed upstream")
    args = parser.parse_args()
    if args.workers < 1:
        parser.error("--workers must be at least 1")
    if args.timeout <= 0:
        parser.error("--timeout must be positive")
    return args


if __name__ == "__main__":
    arguments = parse_args()
    raise SystemExit(mirror(workers=arguments.workers, timeout=arguments.timeout, clean=not arguments.no_clean))
