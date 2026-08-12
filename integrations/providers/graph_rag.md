> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Graph RAG integrations

> Integrate with Graph RAG using LangChain Python.

## Overview

[Graph RAG](https://datastax.github.io/graph-rag/) provides a retriever interface
that combines **unstructured** similarity search on vectors with **structured**
traversal of metadata properties. This enables graph-based retrieval over **existing**
vector stores.

## Installation and setup

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langchain-graph-retriever
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langchain-graph-retriever
  ```
</CodeGroup>

## Retrievers

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_graph_retriever import GraphRetriever
```

For more information, see the [Graph RAG Integration Guide](/oss/python/integrations/retrievers/graph_rag).

***

<div className="source-links">
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/graph_rag.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
