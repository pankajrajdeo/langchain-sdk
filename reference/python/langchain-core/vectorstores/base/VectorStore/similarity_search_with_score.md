---
title: "similarity_search_with_score"
description: "Run similarity search with distance."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/similarity_search_with_score"
category: "reference"
tags: [reference, langchain-core, vectorstores, base, vectorstore, similarity_search_with_score]
---

# similarity_search_with_score

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/similarity_search_with_score)

Run similarity search with distance.

## Signature

```python
similarity_search_with_score(
    self,
    args: Any = (),
    kwargs: Any = {},
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/6419339aa163a49f32d9b80ff20d6adc3b446d49/libs/core/langchain_core/vectorstores/base.py#L417)
