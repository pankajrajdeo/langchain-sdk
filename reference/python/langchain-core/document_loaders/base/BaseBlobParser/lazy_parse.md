---
title: "lazy_parse"
description: "Lazy parsing interface."
source: "https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseBlobParser/lazy_parse"
category: "reference"
tags: [reference, langchain-core, document_loaders, base, baseblobparser, lazy_parse]
---

# lazy_parse

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseBlobParser/lazy_parse)

Lazy parsing interface.

Subclasses are required to implement this method.

## Signature

```python
lazy_parse(
    self,
    blob: Blob,
) -> Iterator[Document]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `blob` | `Blob` | Yes | `Blob` instance |

## Returns

`Iterator[Document]`

Generator of `Document` objects

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/5069b326c53069ec85a7e1d914c6873feb8d0cfa/libs/core/langchain_core/document_loaders/base.py#L127)
