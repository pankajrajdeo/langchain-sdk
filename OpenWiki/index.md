# OpenWiki

> CLI that writes and maintains agent wikis so coding agents work faster

OpenWiki is an open source CLI that writes and maintains a Markdown wiki about your codebase or personal knowledge. The wiki captures details such as architecture, integrations, evals, and workflows so [coding agents](https://docs.langchain.com/oss/python/deepagents/overview) can use it as durable context instead of rediscovering the repository on every task.

That makes agent work faster and cheaper in tokens: agents read a curated wiki first, then inspect source only where they need more detail. Humans can browse the same Markdown (and the local [visualizer](https://docs.langchain.com/oss/openwiki/visualize)), but the primary audience is agents.

OpenWiki is built on [Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview) and supports tracing with [LangSmith](https://docs.langchain.com/langsmith/observability-quickstart).

## Get started

Install the CLI, then initialize documentation for the current repository:

```bash
npm install -g openwiki
openwiki --init
```

See the [Quickstart](https://docs.langchain.com/oss/openwiki/quickstart) to choose a model provider, generate docs, and keep them up to date.

> [!NOTE]
> OpenWiki does not provide a formal connector for Claude or Codex. In code mode, it adds pointers to the generated wiki in the repository-root `AGENTS.md` and `CLAUDE.md` files, so compatible coding agents can discover and consult the wiki.

## Modes

OpenWiki has two modes:

| Mode               | Command                      | Output                                | Use when                                                        |
| ------------------ | ---------------------------- | ------------------------------------- | --------------------------------------------------------------- |
| **Code** (default) | `openwiki` / `openwiki code` | `openwiki/` in the current repository | You want repository context and documentation for coding agents |
| **Personal**       | `openwiki personal`          | `~/.openwiki/wiki`                    | You want a local personal brain from configured sources         |

Bare `openwiki --init` and `openwiki --update` run in code mode. Use `openwiki personal --init` or `openwiki personal --update` for the personal wiki.

## Capabilities

#### [Repository wikis](https://docs.langchain.com/oss/openwiki/code-mode)
Generate Markdown docs under `openwiki/`, then wire them into `AGENTS.md` and `CLAUDE.md` so coding agents can find them.

#### [Personal brain](https://docs.langchain.com/oss/openwiki/personal-mode)
Build a local wiki from git repos, Gmail, Notion, web search, Hacker News, and X/Twitter.

#### [Automatic updates](https://docs.langchain.com/oss/openwiki/automate-updates)
Refresh docs from GitHub Actions, GitLab CI, or Bitbucket Pipelines and open a PR when content changes.

#### [Model providers](https://docs.langchain.com/oss/openwiki/providers)
Use OpenAI, Anthropic, Gemini, Bedrock, OpenRouter, GitHub Copilot, and other providers out of the box.

#### [Open Knowledge Format](https://docs.langchain.com/oss/openwiki/code-mode#open-knowledge-format)
Emit OKF v0.1 Markdown bundles with front matter, indexes, and linked concepts.

#### [LangSmith tracing](https://docs.langchain.com/oss/openwiki/quickstart#trace-with-langsmith)
Trace documentation runs with LangSmith.

## Next steps

#### [Quickstart](https://docs.langchain.com/oss/openwiki/quickstart)
Install OpenWiki, configure a provider, and generate your first wiki.

#### [CLI reference](https://docs.langchain.com/oss/openwiki/cli-reference)
Review commands, flags, and connector subcommands.

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/openwiki/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
