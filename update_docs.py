#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["tqdm>=4.66,<5"]
# ///
"""Mirror selected LangChain documentation as GitHub-friendly Markdown.

Discovery uses the site's sitemap, llms.txt, llms-full.txt, configured entry
points, and links found in downloaded content. Mintlify MDX is normalized to
GitHub Flavored Markdown. Files are written atomically, and only files recorded
in the previous managed manifest are eligible for stale-file cleanup.
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
except ImportError:  # pragma: no cover - depends on the local environment
    tqdm = None  # type: ignore[assignment]


ORIGIN = "https://docs.langchain.com"
SITEMAP_URL = f"{ORIGIN}/sitemap.xml"
LLMS_URL = f"{ORIGIN}/llms.txt"
LLMS_FULL_URL = f"{ORIGIN}/llms-full.txt"
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
LLMS_FULL_PAGE_RE = re.compile(
    r"(?m)^# [^\n]+\nSource: (https://docs\.langchain\.com/\S+)\s*$"
)
GENERATED_COMPONENT_RE = re.compile(
    r"(?m)^export const (PatternEmbed|ExampleEmbed)\s*=.*$"
)
SIMPLE_EXPORT_RE = re.compile(
    r"(?m)^export const (?:protocol|prefix|suffix)_\d+\s*=.*\n?"
)
DOC_INDEX_RE = re.compile(
    r"\A> ## Documentation Index\n"
    r"> Fetch the complete documentation index at: https://docs\.langchain\.com/llms\.txt\n"
    r"> Use this file to discover all available pages before exploring further\.\n*"
)
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
    raw_body: bytes | None = None
    body: bytes | None = None
    content_source: str = "page-markdown"
    normalization_warnings: list[str] | None = None
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


def parse_llms_full(body: bytes) -> dict[str, bytes]:
    """Split llms-full.txt into canonical per-page Markdown documents."""
    text = body.decode("utf-8", errors="replace")
    matches = list(LLMS_FULL_PAGE_RE.finditer(text))
    pages: dict[str, bytes] = {}
    for index, match in enumerate(matches):
        page_url = canonical_page_url(match.group(1))
        if not page_url:
            continue
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page = text[match.start():end].strip()
        if page:
            pages[page_url] = (page + "\n").encode("utf-8")
    return pages


def find_javascript_block_end(text: str, opening_brace: int) -> int | None:
    """Find the end of a generated JS function while respecting strings/comments."""
    depth = 0
    index = opening_brace
    quote: str | None = None
    escaped = False
    line_comment = False
    block_comment = False
    while index < len(text):
        char = text[index]
        following = text[index + 1] if index + 1 < len(text) else ""
        if line_comment:
            if char == "\n":
                line_comment = False
        elif block_comment:
            if char == "*" and following == "/":
                block_comment = False
                index += 1
        elif quote:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = None
        elif char == "/" and following == "/":
            line_comment = True
            index += 1
        elif char == "/" and following == "*":
            block_comment = True
            index += 1
        elif char in {"'", '"', "`"}:
            quote = char
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                index += 1
                while index < len(text) and text[index] in " \t;":
                    index += 1
                while index < len(text) and text[index] == "\n":
                    index += 1
                return index
        index += 1
    return None


def remove_generated_components(text: str) -> tuple[str, list[str]]:
    """Remove component implementation blobs emitted by the Mintlify endpoint."""
    warnings: list[str] = []
    while True:
        match = GENERATED_COMPONENT_RE.search(text)
        if not match:
            break
        arrow = text.find("=>", match.start(), match.end() + 500)
        opening_brace = text.find("{", arrow + 2) if arrow >= 0 else -1
        end = find_javascript_block_end(text, opening_brace) if opening_brace >= 0 else None
        if end is None:
            warnings.append(f"could not safely remove generated {match.group(1)} definition")
            break
        text = text[:match.start()] + text[end:]
    return SIMPLE_EXPORT_RE.sub("", text), warnings


def attribute(tag: str, name: str) -> str | None:
    match = re.search(rf"\b{re.escape(name)}=[\"']([^\"']*)[\"']", tag)
    return match.group(1) if match else None


def absolute_docs_link(target: str, page_url: str) -> str:
    # Mintlify content sometimes omits the leading slash from paths that are
    # nevertheless site-root namespaces (for example `langsmith/llm-gateway`).
    # Treat only known top-level namespaces this way; ordinary names remain
    # correctly relative to the current page.
    if target.startswith(("oss/", "langsmith/", "api-reference/")):
        target = "/" + target
    return urljoin(page_url, target)


def rewrite_markdown_links(text: str, page_url: str) -> str:
    """Make relative Markdown/HTML links reliable when rendered on GitHub."""
    markdown_link = re.compile(r"(?P<prefix>!?\[[^\]]*\]\()(?P<target><[^>]+>|[^)\s]+)")

    def replace_markdown(match: re.Match[str]) -> str:
        target = match.group("target")
        wrapped = target.startswith("<") and target.endswith(">")
        plain = target[1:-1] if wrapped else target
        if plain.startswith(("mailto:", "tel:", "data:", "javascript:")):
            return match.group(0)
        parts = urlsplit(plain)
        if parts.scheme or plain.startswith("//"):
            return match.group(0)
        rewritten = absolute_docs_link(plain, page_url)
        return match.group("prefix") + (f"<{rewritten}>" if wrapped else rewritten)

    text = markdown_link.sub(replace_markdown, text)

    def replace_reference(match: re.Match[str]) -> str:
        target = match.group(2)
        if target.startswith(("mailto:", "tel:", "data:")) or urlsplit(target).scheme:
            return match.group(0)
        return f"{match.group(1)}{absolute_docs_link(target, page_url)}"

    text = re.sub(r"(?m)^(\s*\[[^\]]+\]:\s*)(\S+)", replace_reference, text)

    def replace_html(match: re.Match[str]) -> str:
        target = match.group(3)
        if target.startswith(("mailto:", "tel:", "data:")) or urlsplit(target).scheme:
            return match.group(0)
        return f"{match.group(1)}={match.group(2)}{absolute_docs_link(target, page_url)}{match.group(2)}"

    return re.sub(r"\b(href|src)=(['\"])([^'\"]+)\2", replace_html, text)


def convert_html_link_cards(text: str, page_url: str) -> str:
    """Turn Mintlify's JSX-styled logo cards into simple, durable links."""
    card_re = re.compile(
        r"(?m)^[ \t]*<a\s+([^>]*\bhref=[\"'][^\"']+[\"'][^>]*)>\s*"
        r"(?P<body>(?:<img\b[^>]*/>\s*){1,2}"
        r"<span\b[^>]*>(?P<label>.*?)</span>)\s*</a>[ \t]*$"
    )

    def replace(match: re.Match[str]) -> str:
        href = attribute(match.group(1), "href")
        label = re.sub(r"<[^>]+>", "", match.group("label")).strip()
        if not href or not label:
            return match.group(0)
        return f"- [{label}]({absolute_docs_link(href, page_url)})"

    return card_re.sub(replace, text)


def dedent_mdx_children(text: str) -> str:
    """Remove presentation indentation introduced by nested MDX components."""
    output: list[str] = []
    stack: list[str] = []
    fence: str | None = None
    opening_re = re.compile(r"^<([A-Z][A-Za-z0-9.]*|div)\b[^>]*>$")
    closing_re = re.compile(r"^</([A-Z][A-Za-z0-9.]*|div)>$")

    for line in text.splitlines():
        stripped = line.strip()
        closing = closing_re.fullmatch(stripped)
        if fence is None and closing:
            name = closing.group(1)
            if name in stack:
                reverse_index = stack[::-1].index(name)
                del stack[len(stack) - reverse_index - 1:]

        remove = min(len(line) - len(line.lstrip(" ")), len(stack) * 2)
        adjusted = line[remove:]
        adjusted_stripped = adjusted.strip()
        if adjusted_stripped.startswith(("```", "~~~")):
            marker = adjusted_stripped[:3]
            if fence is None:
                fence = marker
            elif fence == marker:
                fence = None

        output.append(adjusted)
        if fence is None:
            opening = opening_re.fullmatch(stripped)
            if opening and not stripped.endswith("/>") and not re.search(
                rf"</{re.escape(opening.group(1))}>\s*$", stripped
            ):
                stack.append(opening.group(1))
    return "\n".join(output)


def convert_mdx(text: str, page_url: str) -> str:
    """Convert common Mintlify MDX constructs to GitHub Flavored Markdown."""
    lines = text.splitlines()
    output: list[str] = []
    fence: str | None = None
    alerts: list[str] = []
    alert_names = {
        "Tip": "TIP",
        "Note": "NOTE",
        "Info": "NOTE",
        "Callout": "NOTE",
        "Warning": "WARNING",
        "Danger": "CAUTION",
        "Important": "IMPORTANT",
        "Check": "TIP",
    }
    drop_wrappers = {
        "AccordionGroup", "CardGroup", "CodeGroup", "Columns", "Frame",
        "Steps", "Tabs",
    }
    tree_depth = 0
    html_heading_level: int | None = None

    def emit(items: str | list[str]) -> None:
        values = [items] if isinstance(items, str) else items
        prefix = "> " * len(alerts)
        for value in values:
            output.append(prefix + value if value else (prefix.rstrip() if alerts else ""))

    def semantic_media_link(tag_text: str, kind: str) -> str:
        label = (
            attribute(tag_text, "aria-label")
            or attribute(tag_text, "title")
            or f"Embedded {kind}"
        )
        source = attribute(tag_text, "src")
        target = absolute_docs_link(source, page_url) if source else page_url
        return f"> **{kind.title()}:** [{label}]({target})"

    for line in lines:
        stripped = line.strip()
        fence_candidate = stripped.removeprefix("> ")
        if fence_candidate.startswith(("```", "~~~")):
            marker_match = re.match(r"(`{3,}|~{3,})", fence_candidate)
            marker = marker_match.group(1) if marker_match else fence_candidate[:3]
            if fence is None:
                info = fence_candidate[len(marker):].strip()
                language_match = re.match(r"[A-Za-z0-9_+.-]+", info)
                clean_fence = marker + (language_match.group(0) if language_match else "")
                emit(clean_fence)
            else:
                emit(marker)
            if fence is None:
                fence = marker
            elif fence == marker:
                fence = None
            continue
        if fence is not None:
            emit(line)
            continue

        html_heading_open = re.fullmatch(r"<h([1-6])\b[^>]*>", stripped, flags=re.IGNORECASE)
        if html_heading_open:
            html_heading_level = int(html_heading_open.group(1))
            continue
        if html_heading_level is not None:
            if re.fullmatch(rf"</h{html_heading_level}>", stripped, flags=re.IGNORECASE):
                html_heading_level = None
            elif stripped:
                emit(f"{'#' * html_heading_level} {stripped}")
            continue

        # Generated interactive embeds cannot execute on GitHub.
        if re.fullmatch(r"<(?:PatternEmbed|ExampleEmbed)\b[^>]*/>", stripped):
            emit(
                f"> **Interactive example:** [Open it in the original LangChain documentation]({page_url})."
            )
            continue

        if re.fullmatch(r"<a\s*/>", stripped, flags=re.IGNORECASE):
            continue
        image_tag = re.fullmatch(r"<img\b[^>]*/>", stripped, flags=re.IGNORECASE)
        if image_tag and attribute(stripped, "src") is None:
            alt = attribute(stripped, "alt") or "Image"
            emit(f"> **Image:** [{alt}]({page_url})")
            continue
        if re.fullmatch(r"<iframe\b[^>]*(?:/>|>\s*</iframe>)", stripped, flags=re.IGNORECASE):
            emit(semantic_media_link(stripped, "embedded content"))
            continue
        if re.fullmatch(r"<video\b[^>]*>", stripped, flags=re.IGNORECASE):
            emit(semantic_media_link(stripped, "video"))
            continue
        if re.fullmatch(r"</video>", stripped, flags=re.IGNORECASE):
            continue
        if stripped == "Your browser does not support the video tag.":
            continue

        html_heading = re.fullmatch(
            r"<h([1-6])\b[^>]*>(.*?)</h\1>", stripped, flags=re.IGNORECASE
        )
        if html_heading:
            heading = f"{'#' * int(html_heading.group(1))} {html_heading.group(2).strip()}"
            if heading not in output:
                emit(heading)
            continue

        if re.fullmatch(r"<important\b[^>]*>", stripped, flags=re.IGNORECASE):
            alerts.append("Important")
            emit("[!IMPORTANT]")
            continue
        if re.fullmatch(r"</important>", stripped, flags=re.IGNORECASE):
            if alerts and alerts[-1] == "Important":
                alerts.pop()
            emit("")
            continue

        open_tag = re.fullmatch(r"<([A-Z][A-Za-z0-9.]*)\b([^>]*)>", stripped)
        close_tag = re.fullmatch(r"</([A-Z][A-Za-z0-9.]*)>", stripped)
        self_closing = re.fullmatch(r"<([A-Z][A-Za-z0-9.]*)\b([^>]*)/>", stripped)

        if open_tag and open_tag.group(1) in alert_names:
            name = open_tag.group(1)
            alerts.append(name)
            emit(f"[!{alert_names[name]}]")
            title = attribute(stripped, "title")
            if title:
                emit(f"**{title}**")
            continue
        if close_tag and alerts and close_tag.group(1) == alerts[-1]:
            alerts.pop()
            emit("")
            continue

        if open_tag and open_tag.group(1) == "Tree":
            tree_depth = 0
            continue
        if close_tag and close_tag.group(1) == "Tree":
            tree_depth = 0
            emit("")
            continue
        if open_tag and open_tag.group(1) == "Tree.Folder":
            name = attribute(stripped, "name") or "folder"
            emit(f"{'  ' * tree_depth}- 📁 `{name}/`")
            tree_depth += 1
            continue
        if close_tag and close_tag.group(1) == "Tree.Folder":
            tree_depth = max(0, tree_depth - 1)
            continue
        if self_closing and self_closing.group(1) == "Tree.File":
            name = attribute(stripped, "name") or "file"
            emit(f"{'  ' * tree_depth}- 📄 `{name}`")
            continue

        if open_tag and open_tag.group(1) == "Prompt":
            description = attribute(stripped, "description") or "Example prompt"
            emit(f"> **Prompt:** {description}")
            continue
        if self_closing and self_closing.group(1) == "Prompt":
            description = attribute(stripped, "description") or "Example prompt"
            emit(f"> **Prompt:** {description}")
            continue
        if close_tag and close_tag.group(1) == "Prompt":
            continue

        if (open_tag and open_tag.group(1) in drop_wrappers) or (
            close_tag and close_tag.group(1) in drop_wrappers
        ):
            continue

        if open_tag and open_tag.group(1) == "Tab":
            emit(f"#### {attribute(stripped, 'title') or 'Option'}")
            continue
        if close_tag and close_tag.group(1) == "Tab":
            continue

        if open_tag and open_tag.group(1) == "Card":
            title = attribute(stripped, "title") or "Related documentation"
            href = attribute(stripped, "href")
            heading = f"#### [{title}]({absolute_docs_link(href, page_url)})" if href else f"#### {title}"
            emit(heading)
            continue
        if self_closing and self_closing.group(1) == "Card":
            title = attribute(stripped, "title") or "Related documentation"
            href = attribute(stripped, "href")
            emit(f"- [{title}]({absolute_docs_link(href, page_url)})" if href else f"- **{title}**")
            continue
        if close_tag and close_tag.group(1) == "Card":
            continue

        if open_tag and open_tag.group(1) == "Accordion":
            title = attribute(stripped, "title") or "Details"
            emit(["<details>", f"<summary>{title}</summary>", ""])
            continue
        if close_tag and close_tag.group(1) == "Accordion":
            emit(["", "</details>"])
            continue

        if open_tag and open_tag.group(1) == "Step":
            emit(f"### {attribute(stripped, 'title') or 'Step'}")
            continue
        if close_tag and close_tag.group(1) == "Step":
            continue

        if open_tag and open_tag.group(1) == "Update":
            emit(f"## {attribute(stripped, 'label') or 'Update'}")
            continue
        if close_tag and close_tag.group(1) == "Update":
            continue

        if open_tag and open_tag.group(1) in {"ParamField", "ResponseField"}:
            name = attribute(stripped, "path") or attribute(stripped, "name") or "Field"
            kind = attribute(stripped, "type")
            emit(f"#### `{name}`{f' — `{kind}`' if kind else ''}")
            continue
        if close_tag and close_tag.group(1) in {"ParamField", "ResponseField"}:
            continue

        # Remove standalone layout divs; their children remain intact.
        if re.fullmatch(r"</?div(?:\s[^>]*)?>", stripped, flags=re.IGNORECASE):
            continue

        # Preserve the content of remaining inline MDX while dropping tags that
        # GitHub cannot execute. Standalone labeled components become headings.
        if open_tag or self_closing:
            tag_text = stripped
            title = attribute(tag_text, "title") or attribute(tag_text, "label")
            href = attribute(tag_text, "href")
            if title and href:
                emit(f"**[{title}]({absolute_docs_link(href, page_url)})**")
            elif title:
                emit(f"**{title}**")
            elif self_closing and self_closing.group(1) not in {"Anchor", "Icon"}:
                note = (
                    f"> **Interactive content:** [View this section in the original "
                    f"documentation]({page_url})."
                )
                if not output or output[-1] != note:
                    emit(note)
            continue
        if close_tag:
            continue

        cleaned = re.sub(r"</?[A-Z][A-Za-z0-9.]*\b[^>]*>", "", line)
        cleaned = re.sub(r"\s+style=\{\{.*?\}\}", "", cleaned)
        cleaned = re.sub(r"\s+className=(?:\{[^}]*\}|[\"'][^\"']*[\"'])", "", cleaned)
        cleaned = re.sub(r"\s+noZoom(?=\s|/?>)", "", cleaned)
        cleaned = re.sub(r"\bautoPlay\b", "autoplay", cleaned)
        cleaned = re.sub(r"\bplaysInline\b", "playsinline", cleaned)
        emit(cleaned)

    return "\n".join(output)


def normalize_markdown(raw_body: bytes, page_url: str) -> tuple[bytes, list[str]]:
    text = raw_body.decode("utf-8")
    text = DOC_INDEX_RE.sub("", text)
    text, warnings = remove_generated_components(text)
    text = dedent_mdx_children(text)
    text = convert_html_link_cards(text, page_url)
    text = re.sub(
        r"(?m)^Source: (https://docs\.langchain\.com/\S+)\s*$",
        r"> Source: [Original LangChain documentation](\1)",
        text,
    )
    text = convert_mdx(text, page_url)
    text = rewrite_markdown_links(text, page_url)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    warnings.extend(validate_gfm(text))
    return text.encode("utf-8"), warnings


def validate_gfm(text: str) -> list[str]:
    """Return structural issues that would make GitHub rendering unreliable."""
    warnings: list[str] = []
    fence: str | None = None
    for number, line in enumerate(text.splitlines(), 1):
        stripped = line.lstrip()
        marker_match = re.match(r"(`{3,}|~{3,})", stripped)
        if marker_match:
            marker = marker_match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            continue
        if fence is not None:
            continue
        if re.search(r"</?[A-Z][A-Za-z0-9.]*\b", line):
            warnings.append(f"line {number}: unconverted MDX component")
        if re.match(r"\s*export const\b", line):
            warnings.append(f"line {number}: generated JavaScript export")
        if "className=" in line or "style={{" in line:
            warnings.append(f"line {number}: unconverted JSX attribute")

        for match in re.finditer(r"!?\[[^\]]*\]\((<[^>]+>|[^)\s]+)", line):
            target = match.group(1).strip("<>")
            if target.startswith(("mailto:", "tel:", "data:", "javascript:")):
                continue
            if not urlsplit(target).scheme and not target.startswith("//"):
                warnings.append(f"line {number}: relative Markdown link")
                break

        for match in re.finditer(r"\b(?:href|src)=['\"]([^'\"]+)['\"]", line):
            target = match.group(1)
            if target.startswith(("mailto:", "tel:", "data:")):
                continue
            if not urlsplit(target).scheme and not target.startswith("//"):
                warnings.append(f"line {number}: relative HTML link")
                break
    if fence is not None:
        warnings.append("unclosed fenced code block")
    return warnings[:20]


def discover_seed_urls(timeout: float) -> tuple[set[str], dict[str, bytes], list[str]]:
    pages = {
        canonical_page_url(section.entry_url)
        for section in SECTIONS
        if section.entry_url is not None
    }
    errors: list[str] = []
    full_pages: dict[str, bytes] = {}

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

    try:
        llms_full, _, _ = request_bytes(LLMS_FULL_URL, timeout)
        full_pages = parse_llms_full(llms_full)
        pages.update(full_pages)
    except Exception as exc:
        errors.append(f"llms-full.txt content discovery: {exc}")

    return {page for page in pages if page}, full_pages, errors


def download_one(page_url: str, timeout: float, full_pages: dict[str, bytes]) -> Download:
    if page_url in full_pages:
        raw_body = full_pages[page_url]
        body, warnings = normalize_markdown(raw_body, page_url)
        return Download(
            page_url=page_url,
            final_url=LLMS_FULL_URL,
            raw_body=raw_body,
            body=body,
            content_source="llms-full.txt",
            normalization_warnings=warnings,
        )
    try:
        raw_body, final_url, content_type = request_bytes(markdown_url(page_url), timeout)
        if urlsplit(final_url).netloc.lower() != "docs.langchain.com":
            return Download(page_url=page_url, final_url=final_url, skipped="redirects outside docs.langchain.com")
        prefix = raw_body[:200].lstrip().lower()
        if content_type == "text/html" or prefix.startswith((b"<!doctype html", b"<html")):
            raise RuntimeError("server returned HTML instead of Markdown")
        raw_body.decode("utf-8")
        body, warnings = normalize_markdown(raw_body, page_url)
        return Download(
            page_url=page_url,
            final_url=final_url,
            raw_body=raw_body,
            body=body,
            normalization_warnings=warnings,
        )
    except ExternalRedirect as exc:
        return Download(page_url=page_url, final_url=exc.url, skipped="redirects outside docs.langchain.com")
    except (RuntimeError, UnicodeDecodeError) as exc:
        return Download(page_url=page_url, error=str(exc))


def links_from(download: Download) -> set[str]:
    source_body = download.raw_body or download.body
    if source_body is None:
        return set()
    text = source_body.decode("utf-8")
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
    if tqdm is None:  # pragma: no cover - depends on the local environment
        uv = shutil.which("uv")
        if uv:
            os.execv(uv, [uv, "run", "--script", str(Path(__file__).resolve()), *sys.argv[1:]])
        raise SystemExit(
            "Missing dependency: install it with `python3 -m pip install tqdm`, "
            "or install uv so this script can provision tqdm automatically."
        )
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    for section in SECTIONS:
        directory = OUTPUT_ROOT / section.folder
        if section.local_subfolder:
            directory /= section.local_subfolder
        directory.mkdir(parents=True, exist_ok=True)

    seeds, full_pages, discovery_errors = discover_seed_urls(timeout)
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
                futures = {
                    executor.submit(download_one, page, timeout, full_pages): page
                    for page in batch
                }
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
    normalization_warnings: dict[str, list[str]] = {}
    for page_url, result in sorted(completed.items()):
        path = local_path_for(page_url)
        body = result.body or b""
        raw_body = result.raw_body or body
        files[relative_output_path(path)] = {
            "source": page_url,
            "resolved_markdown": result.final_url or markdown_url(page_url),
            "bytes": len(body),
            "sha256": hashlib.sha256(body).hexdigest(),
            "upstream_bytes": len(raw_body),
            "upstream_sha256": hashlib.sha256(raw_body).hexdigest(),
            "content_source": result.content_source,
        }
        if result.normalization_warnings:
            normalization_warnings[page_url] = result.normalization_warnings

    previous = load_previous_manifest()
    removed = clean_stale_files(previous, set(files)) if clean and not failures else []
    manifest = {
        "schema_version": 2,
        "source": ORIGIN,
        "page_count": len(files),
        "files": files,
        "failures": failures,
        "broken_or_non_page_links": broken_links,
        "external_redirects": skipped,
        "normalization_warnings": normalization_warnings,
        "llms_full_page_count": len(full_pages),
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
    print(f"Used llms-full.txt for {sum(r.content_source == 'llms-full.txt' for r in completed.values())} pages.")
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
    if normalization_warnings:
        print(f"Normalization warnings in {len(normalization_warnings)} pages.", file=sys.stderr)
        return 1
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
