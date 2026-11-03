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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/e936943647fe9bd9c4c24122ee3e1812ead82130/libs/core/langchain_core/embeddings/embeddings.py#L69)
