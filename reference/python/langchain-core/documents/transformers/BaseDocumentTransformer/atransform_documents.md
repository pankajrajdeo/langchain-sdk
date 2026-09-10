---
title: "atransform_documents"
description: "Asynchronously transform a list of documents."
source: "https://reference.langchain.com/python/langchain-core/documents/transformers/BaseDocumentTransformer/atransform_documents"
category: "reference"
tags: [reference, langchain-core, documents, transformers, basedocumenttransformer, atransform_documents]
---

# atransform_documents

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/documents/transformers/BaseDocumentTransformer/atransform_documents)

Asynchronously transform a list of documents.

## Signature

```python
atransform_documents(
    self,
    documents: Sequence[Document],
    **kwargs: Any = {},
) -> Sequence[Document]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `documents` | `Sequence[Document]` | Yes | A sequence of `Document` objects to be transformed. |

## Returns

`Sequence[Document]`

A sequence of transformed `Document` objects.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/documents/transformers.py#L66)
