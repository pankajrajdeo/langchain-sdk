---
title: "similarity_search_by_vector"
description: "Return docs most similar to embedding vector."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/similarity_search_by_vector"
category: "reference"
tags: [reference, langchain-core, vectorstores, base, vectorstore, similarity_search_by_vector]
---

# similarity_search_by_vector

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/similarity_search_by_vector)

Return docs most similar to embedding vector.

## Signature

```python
similarity_search_by_vector(
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/vectorstores/base.py#L624)
