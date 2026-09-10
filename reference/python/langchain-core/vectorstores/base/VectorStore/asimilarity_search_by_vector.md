---
title: "asimilarity_search_by_vector"
description: "Async return docs most similar to embedding vector."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/asimilarity_search_by_vector"
category: "reference"
tags: [reference, langchain-core, vectorstores, base, vectorstore, asimilarity_search_by_vector]
---

# asimilarity_search_by_vector

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/asimilarity_search_by_vector)

Async return docs most similar to embedding vector.

## Signature

```python
asimilarity_search_by_vector(
    self,
    embedding: list[float],
    k: int = 4,
    **kwargs: Any = {},
) -> list[Document]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `embedding` | `list[float]` | Yes | Embedding to look up documents similar to. |
| `k` | `int` | No | Number of `Document` objects to return. (default: `4`) |
| `**kwargs` | `Any` | No | Arguments to pass to the search method. (default: `{}`) |

## Returns

`list[Document]`

List of `Document` objects most similar to the query vector.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/vectorstores/base.py#L639)
