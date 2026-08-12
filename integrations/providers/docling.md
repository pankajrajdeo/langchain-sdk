> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Docling integrations

> Integrate with Docling using LangChain Python.

> [Docling](https://github.com/DS4SD/docling) parses PDF, DOCX, PPTX, HTML, and other formats into a rich unified representation including document layout, tables etc., making them ready for generative AI workflows like RAG.
>
> This integration provides Docling's capabilities via the `DoclingLoader` document loader.

## Installation and setup

Simply install `langchain-docling` from your package manager, e.g. pip:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langchain-docling
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langchain-docling
  ```
</CodeGroup>

## Document loader

The `DoclingLoader` class in `langchain-docling` seamlessly integrates Docling into
LangChain, enabling you to:

* use various document types in your LLM applications with ease and speed, and
* leverage Docling's rich representation for advanced, document-native grounding.

Basic usage looks as follows:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_docling import DoclingLoader

FILE_PATH = ["https://arxiv.org/pdf/2408.09869"]  # Docling Technical Report

loader = DoclingLoader(file_path=FILE_PATH)

docs = loader.load()
```

For end-to-end usage check out
[this example](/oss/python/integrations/document_loaders/docling).

## Additional resources

* [LangChain Docling integration GitHub](https://github.com/DS4SD/docling-langchain)
* [LangChain Docling integration PyPI package](https://pypi.org/project/langchain-docling/)
* [Docling GitHub](https://github.com/DS4SD/docling)
* [Docling docs](https://ds4sd.github.io/docling/)

***

<div className="source-links">
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/docling.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
