---
title: "embed_documents"
description: "Embed search docs."
source: "https://reference.langchain.com/python/langchain-core/embeddings/embeddings/Embeddings/embed_documents"
category: "reference"
tags: [reference, langchain-core, embeddings, embed_documents]
---

# embed_documents

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/embeddings/embeddings/Embeddings/embed_documents)

Embed search docs.

## Signature

```python
embed_documents(
    self,
    texts: list[str],
) -> list[list[float]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `texts` | `list[str]` | Yes | List of text to embed. |

## Returns

`list[list[float]]`

List of embeddings.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/embeddings/embeddings.py#L36)
