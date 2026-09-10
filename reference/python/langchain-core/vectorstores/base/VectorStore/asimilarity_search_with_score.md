---
title: "asimilarity_search_with_score"
description: "Async run similarity search with distance."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/asimilarity_search_with_score"
category: "reference"
tags: [reference, langchain-core, vectorstores, base, vectorstore, asimilarity_search_with_score]
---

# asimilarity_search_with_score

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/asimilarity_search_with_score)

Async run similarity search with distance.

## Signature

```python
asimilarity_search_with_score(
    self,
    *args: Any = (),
    **kwargs: Any = {},
) -> list[tuple[Document, float]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `*args` | `Any` | No | Arguments to pass to the search method. (default: `()`) |
| `**kwargs` | `Any` | No | Arguments to pass to the search method. (default: `{}`) |

## Returns

`list[tuple[Document, float]]`

List of tuples of `(doc, similarity_score)`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/vectorstores/base.py#L431)
