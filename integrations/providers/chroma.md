> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Chroma integrations

> Integrate with Chroma using LangChain Python.

> [Chroma](https://docs.trychroma.com/getting-started) is a database for building AI applications with embeddings.

## Installation and setup

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langchain-chroma
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langchain-chroma
  ```
</CodeGroup>

## VectorStore

There exists a wrapper around Chroma vector databases, allowing you to use it as a vectorstore,
whether for semantic search or example selection.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_chroma import Chroma
```

For a more detailed walkthrough of the Chroma wrapper, see [this notebook](/oss/python/integrations/vectorstores/chroma).

## Retriever

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_classic.retrievers import SelfQueryRetriever
```

***

<div className="source-links">
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/chroma.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
