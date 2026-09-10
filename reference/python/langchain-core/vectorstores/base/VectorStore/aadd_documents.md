---
title: "aadd_documents"
description: "Async run more documents through the embeddings and add to the VectorStore."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/aadd_documents"
category: "reference"
tags: [reference, langchain-core, vectorstores, base, vectorstore, aadd_documents]
---

# aadd_documents

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/aadd_documents)

Async run more documents through the embeddings and add to the `VectorStore`.

## Signature

```python
aadd_documents(
    self,
    documents: list[Document],
    **kwargs: Any = {},
) -> list[str]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `documents` | `list[Document]` | Yes | Documents to add to the `VectorStore`. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

## Returns

`list[str]`

List of IDs of the added texts.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/vectorstores/base.py#L265)
