---
title: "invoke"
description: "Invoke the retriever to get relevant documents."
source: "https://reference.langchain.com/python/langchain-core/retrievers/BaseRetriever/invoke"
category: "reference"
tags: [reference, langchain-core, retrievers, baseretriever, invoke]
---

# invoke

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/retrievers/BaseRetriever/invoke)

Invoke the retriever to get relevant documents.

Main entry point for synchronous retriever invocations.

## Signature

```python
invoke(
    self,
    input: str,
    config: RunnableConfig | None = None,
    **kwargs: Any = {},
) -> list[Document]
```

## Description

Examples:
```python
retriever.invoke("query")
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input` | `str` | Yes | The query string. |
| `config` | `RunnableConfig \| None` | No | Configuration for the retriever. (default: `None`) |
| `**kwargs` | `Any` | No | Additional arguments to pass to the retriever. (default: `{}`) |

## Returns

`list[Document]`

List of relevant documents.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/04ac76c07ec173a44e3e57de54861d0b637e3299/libs/core/langchain_core/retrievers.py#L178)
