# LangChain SDK documentation mirror

This repository is an automatically updated Markdown mirror of selected
[LangChain documentation](https://docs.langchain.com/), including the complete
[`/oss/python`](https://docs.langchain.com/oss/python) namespace.

The mirror preserves URL hierarchy: a page such as
`/oss/python/langchain/agents` is stored as `langchain/agents.md`. New Python
SDK categories and nested pages are discovered and created automatically.

## Included documentation

- Complete `/oss/python` documentation, discovered dynamically
- Deep Agents Code documentation from `/oss/deepagents`
- OpenWiki documentation from `/oss/openwiki`
- LangSmith documentation from `/langsmith`

Discovery starts with `llms.txt` and `llms-full.txt`, then combines the
LangChain sitemap, configured entry points, and recursive links found inside
downloaded Markdown. Each page's dedicated `.md` endpoint is the authoritative
content source; `llms-full.txt` is retained as a fallback if that endpoint is
temporarily unavailable. This lets newly published URL categories and
arbitrarily deep subdirectories appear automatically on the next run without
being held back by a stale aggregate index.

The updater converts Mintlify MDX into GitHub Flavored Markdown. Tabs, code
groups, callouts, cards, accordions, file trees, prompts, interactive embeds,
JSX attributes, and links are normalized so their contents remain readable on
GitHub. Citations between successfully mirrored documents use repository-local
relative `.md` paths, including section fragments. Links to documentation that
is outside the configured mirror remain on the official website. Explicit
"original documentation" and interactive-widget links also remain official.

The generated `.mirror-manifest.json` records each source and resolved URL,
normalized and upstream byte sizes and SHA-256 checksums, content source, crawl
failures, and normalization warnings. A run exits unsuccessfully if it leaves
unclosed code fences, executable MDX, JSX attributes, malformed relative links,
or local links whose mirrored target file does not exist.

## Update locally

Python 3.10 or newer is required. Run:

```bash
python3 update_docs.py
```

The script uses `tqdm` for progress. If `tqdm` is unavailable and `uv` is
installed, the script provisions it automatically. Otherwise install it first:

```bash
python3 -m pip install tqdm
```

Useful options:

```bash
python3 update_docs.py --workers 12 --timeout 30
python3 update_docs.py --no-clean
```

Updates are atomic. Stale files are removed only when they were listed in the
previous managed manifest and the current crawl completes without required-page
failures.

Run the normalization regression tests with:

```bash
python3 -m unittest discover -s tests
```

## Automatic updates

The `Update LangChain documentation` GitHub Actions workflow runs daily and can
also be started manually from the Actions tab. When upstream documentation
changes, the workflow commits the refreshed mirror to `main`.

This is an unofficial mirror. LangChain and its documentation belong to their
respective owners.
