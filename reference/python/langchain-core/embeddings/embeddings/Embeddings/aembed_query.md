---
title: "aembed_query"
description: "Asynchronous Embed query text."
source: "https://reference.langchain.com/python/langchain-core/embeddings/embeddings/Embeddings/aembed_query"
category: "reference"
tags: [reference, langchain-core, embeddings, aembed_query]
---

# aembed_query

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/embeddings/embeddings/Embeddings/aembed_query)

Asynchronous Embed query text.

## Signature

```python
aembed_query(
    self,
    text: str,
) -> list[float]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | `str` | Yes | Text to embed. |

## Returns

`list[float]`

Embedding.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/embeddings/embeddings.py#L69)
