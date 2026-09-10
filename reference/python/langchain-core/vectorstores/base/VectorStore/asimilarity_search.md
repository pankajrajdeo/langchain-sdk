---
title: "asimilarity_search"
description: "Async return docs most similar to query."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/asimilarity_search"
category: "reference"
tags: [reference, langchain-core, vectorstores, base, vectorstore, asimilarity_search]
---

# asimilarity_search

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/asimilarity_search)

Async return docs most similar to query.

## Signature

```python
asimilarity_search(
    self,
    query: str,
    k: int = 4,
    **kwargs: Any = {},
) -> list[Document]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | `str` | Yes | Input text. |
| `k` | `int` | No | Number of `Document` objects to return. (default: `4`) |
| `**kwargs` | `Any` | No | Arguments to pass to the search method. (default: `{}`) |

## Returns

`list[Document]`

List of `Document` objects most similar to the query.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/vectorstores/base.py#L606)
