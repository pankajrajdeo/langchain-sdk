---
title: "afrom_documents"
description: "Async return VectorStore initialized from documents and embeddings."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/afrom_documents"
category: "reference"
tags: [reference, langchain-core, vectorstores, base, vectorstore, afrom_documents]
---

# afrom_documents

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/afrom_documents)

Async return `VectorStore` initialized from documents and embeddings.

## Signature

```python
afrom_documents(
    cls,
    documents: list[Document],
    embedding: Embeddings,
    **kwargs: Any = {},
) -> Self
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `documents` | `list[Document]` | Yes | List of `Document` objects to add to the `VectorStore`. |
| `embedding` | `Embeddings` | Yes | Embedding function to use. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

## Returns

`Self`

`VectorStore` initialized from documents and embeddings.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/vectorstores/base.py#L816)
