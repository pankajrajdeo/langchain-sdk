---
title: "compress_documents"
description: "Compress retrieved documents given the query context."
source: "https://reference.langchain.com/python/langchain-core/documents/compressor/BaseDocumentCompressor/compress_documents"
category: "reference"
tags: [reference, langchain-core, documents, compressor, basedocumentcompressor, compress_documents]
---

# compress_documents

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/documents/compressor/BaseDocumentCompressor/compress_documents)

Compress retrieved documents given the query context.

## Signature

```python
compress_documents(
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/documents/compressor.py#L36)
