---
title: "aembed_documents"
description: "Asynchronous Embed search docs."
source: "https://reference.langchain.com/python/langchain-core/embeddings/embeddings/Embeddings/aembed_documents"
category: "reference"
tags: [reference, langchain-core, embeddings, aembed_documents]
---

# aembed_documents

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/embeddings/embeddings/Embeddings/aembed_documents)

Asynchronous Embed search docs.

## Signature

```python
aembed_documents(
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/embeddings/embeddings.py#L58)
