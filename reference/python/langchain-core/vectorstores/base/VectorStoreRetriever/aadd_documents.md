---
title: "aadd_documents"
description: "Async add documents to the VectorStore."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStoreRetriever/aadd_documents"
category: "reference"
tags: [reference, langchain-core, vectorstores, base, vectorstoreretriever, aadd_documents]
---

# aadd_documents

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStoreRetriever/aadd_documents)

Async add documents to the `VectorStore`.

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
| `**kwargs` | `Any` | No | Other keyword arguments that subclasses might use. (default: `{}`) |

## Returns

`list[str]`

List of IDs of the added texts.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/vectorstores/base.py#L1099)
