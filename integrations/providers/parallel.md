# Parallel integrations

> Integrate with Parallel using LangChain Python.

This page covers all LangChain integrations with [Parallel](https://platform.parallel.ai/).

## Installation and setup

The `Parallel` integration lives in its own [partner package](https://pypi.org/project/langchain-parallel/):

```bash
pip install -U langchain-parallel
```

```bash
uv add langchain-parallel
```

Set the `PARALLEL_API_KEY` environment variable to your Parallel API key. Sign up at [platform.parallel.ai](https://platform.parallel.ai) to obtain one.

## Chat models

#### [ChatParallel](https://docs.langchain.com/oss/python/integrations/chat/parallel)
OpenAI-compatible chat model with optional web research and per-field citations on the research tiers.

## Tools

#### [ParallelSearchTool](https://docs.langchain.com/oss/python/integrations/tools/parallel_search)
Search the web and get structured, LLM-optimized excerpts back.

#### [ParallelExtractTool](https://docs.langchain.com/oss/python/integrations/tools/parallel_extract)
Extract clean markdown content from a list of URLs.

#### [ParallelFindAllTool](https://docs.langchain.com/oss/python/integrations/tools/parallel_findall)
Discover entities that satisfy a set of boolean match conditions.

#### [Task API](https://docs.langchain.com/oss/python/integrations/tools/parallel_task)
Run research-grade tasks: single ad-hoc, deep research, batch enrichment. `ParallelTaskRunTool`, `ParallelDeepResearch`, `ParallelTaskGroup`, `ParallelEnrichment`.

#### [ParallelMonitor](https://docs.langchain.com/oss/python/integrations/tools/parallel_monitor)
Schedule a query on a recurring cadence and receive events when relevant new content shows up.

## Retrievers

#### [ParallelSearchRetriever](https://docs.langchain.com/oss/python/integrations/retrievers/parallel)
`BaseRetriever` over Parallel Search. Returns `list[Document]` for drop-in use in any RAG pipeline.

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/parallel.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
