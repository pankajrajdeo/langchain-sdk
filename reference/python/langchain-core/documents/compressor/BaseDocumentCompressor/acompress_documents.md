---
title: "acompress_documents"
description: "Async compress retrieved documents given the query context."
source: "https://reference.langchain.com/python/langchain-core/documents/compressor/BaseDocumentCompressor/acompress_documents"
category: "reference"
tags: [reference, langchain-core, documents, compressor, basedocumentcompressor, acompress_documents]
---

# acompress_documents

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/documents/compressor/BaseDocumentCompressor/acompress_documents)

Async compress retrieved documents given the query context.

## Signature

```python
acompress_documents(
    self,
    documents: Sequence[Document],
    query: str,
    callbacks: Callbacks | None = None,
) -> Sequence[Document]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `documents` | `Sequence[Document]` | Yes | The retrieved `Document` objects. |
| `query` | `str` | Yes | The query context. |
| `callbacks` | `Callbacks \| None` | No | Optional `Callbacks` to run during compression. (default: `None`) |

## Returns

`Sequence[Document]`

The compressed documents.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/documents/compressor.py#L55)
