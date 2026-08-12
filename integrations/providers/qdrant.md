> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Qdrant integrations

> Integrate with Qdrant using LangChain Python.

> [Qdrant](https://qdrant.tech/documentation/) (read: quadrant) is a vector similarity search engine.
> It provides a production-ready service with a convenient API to store, search, and manage
> points - vectors with an additional payload. `Qdrant` is tailored to extended filtering support.

## Installation and setup

Install the Python partner package:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langchain-qdrant
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langchain-qdrant
  ```
</CodeGroup>

## Embedding models

### FastEmbedSparse

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_qdrant import FastEmbedSparse
```

### SparseEmbeddings

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_qdrant import SparseEmbeddings
```

## Vector store

There exists a wrapper around `Qdrant` indexes, allowing you to use it as a vectorstore,
whether for semantic search or example selection.

To import this vectorstore:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_qdrant import QdrantVectorStore
```

For a more detailed walkthrough of the Qdrant wrapper, see [this notebook](/oss/python/integrations/vectorstores/qdrant)

***

<div className="source-links">
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/qdrant.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
