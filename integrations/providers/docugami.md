> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Docugami integrations

> Integrate with Docugami using LangChain Python.

> [Docugami](https://docugami.com) converts business documents into a Document XML Knowledge Graph, generating forests
> of XML semantic trees representing entire documents. This is a rich representation that includes the semantic and
> structural characteristics of various chunks in the document as an XML tree.

## Installation and setup

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install dgml-utils
  pip install docugami-langchain
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add dgml-utils
  uv add docugami-langchain
  ```
</CodeGroup>

## Document loader

See a [usage example](/oss/python/integrations/document_loaders/docugami).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from docugami_langchain.document_loaders import DocugamiLoader
```

***

<div className="source-links">
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/docugami.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
