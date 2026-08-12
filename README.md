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

Discovery combines the LangChain sitemap, `llms.txt`, configured entry points,
and recursive links found inside downloaded Markdown. The generated
`.mirror-manifest.json` records sources, resolved URLs, byte sizes, and SHA-256
checksums for every managed page.

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

## Automatic updates

The `Update LangChain documentation` GitHub Actions workflow runs daily and can
also be started manually from the Actions tab. When upstream documentation
changes, the workflow commits the refreshed mirror to `main`.

This is an unofficial mirror. LangChain and its documentation belong to their
respective owners.
