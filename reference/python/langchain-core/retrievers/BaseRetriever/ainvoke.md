---
title: "ainvoke"
description: "Asynchronously invoke the retriever to get relevant documents."
source: "https://reference.langchain.com/python/langchain-core/retrievers/BaseRetriever/ainvoke"
category: "reference"
tags: [reference, langchain-core, retrievers, baseretriever, ainvoke]
---

# ainvoke

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/retrievers/BaseRetriever/ainvoke)

Asynchronously invoke the retriever to get relevant documents.

Main entry point for asynchronous retriever invocations.

## Signature

```python
ainvoke(
    self,
    input: str,
    config: RunnableConfig | None = None,
    kwargs: Any = {},
) -> list[Document]
```

## Description

Examples:
```python
await retriever.ainvoke("query")
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/retrievers.py#L236)
