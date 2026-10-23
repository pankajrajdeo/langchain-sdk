---
title: "parse"
description: "Eagerly parse the blob into a Document or list of Document objects."
source: "https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseBlobParser/parse"
category: "reference"
tags: [reference, langchain-core, document_loaders, base, baseblobparser, parse]
---

# parse

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseBlobParser/parse)

Eagerly parse the blob into a `Document` or list of `Document` objects.

This is a convenience method for interactive development environment.

Production applications should favor the `lazy_parse` method instead.

Subclasses should generally not over-ride this parse method.

## Signature

```python
parse(
    self,
    blob: Blob,
) -> list[Document]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `blob` | `Blob` | Yes | `Blob` instance |

## Returns

`list[Document]`

List of `Document` objects

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/bdf0f53ed0aec3c9ae371a549e1a4d2ee4e9f021/libs/core/langchain_core/document_loaders/base.py#L140)
