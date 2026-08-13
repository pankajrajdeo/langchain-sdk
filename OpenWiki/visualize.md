# Visualize your wiki

> Explore an OpenWiki Markdown wiki with a local interactive node graph and reader

For exploring OpenWiki Markdown wikis, `openwiki visualize` serves a local interactive node graph beside a live Markdown reader in your browser.

## Open the visualizer

From a repository that already has an `openwiki/` directory:

```bash
openwiki visualize
```

This serves `./openwiki` on `127.0.0.1:4321` and opens your browser to the graph. Edits to wiki files are picked up automatically while the server runs.

## Options

```bash
openwiki visualize openwiki --port 4400 --no-open
```

| Argument / flag | Description                                                                  |
| --------------- | ---------------------------------------------------------------------------- |
| `[path]`        | Wiki directory to serve. Defaults to `./openwiki`                            |
| `--port <port>` | Preferred port. Defaults to `4321`. Increments if the port is already in use |
| `--no-open`     | Do not open the browser automatically                                        |

To explore a personal wiki:

```bash
openwiki visualize ~/.openwiki/wiki
```

<img src="https://mintcdn.com/langchain-5e9cc07a/BPy4qr0YTTF2625M/oss/images/openwiki/visualizer.gif?s=fe0362d13c1436c8a9f1a95cc864c447" alt="OpenWiki visualizer with an interactive node graph beside a live Markdown reader" width="880" height="498" data-path="oss/images/openwiki/visualizer.gif" />

The visualizer shows:

* An interactive node graph of wiki concepts and the Markdown links between them
* A side-by-side live Markdown reader for the selected page

The graph does not show `INSTRUCTIONS.md` and other scaffolding files.

## See also

* [Quickstart](quickstart.md)
* [Code mode](code-mode.md)
* [CLI reference](cli-reference.md)

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/openwiki/visualize.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
