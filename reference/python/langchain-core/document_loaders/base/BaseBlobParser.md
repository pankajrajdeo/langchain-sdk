---
title: "BaseBlobParser"
description: "Abstract interface for blob parsers."
source: "https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseBlobParser"
category: "reference"
tags: [reference, langchain-core, document_loaders, base, baseblobparser]
---

# BaseBlobParser

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseBlobParser)

Abstract interface for blob parsers.

A blob parser provides a way to parse raw data stored in a blob into one or more
`Document` objects.

The parser can be composed with blob loaders, making it easy to reuse a parser
independent of how the blob was originally loaded.

## Signature

```python
BaseBlobParser()
```

## Extends

- `ABC`

## Methods

- [`lazy_parse()`](https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseBlobParser/lazy_parse)
- [`parse()`](https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseBlobParser/parse)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ea17e48f0a4336c920394fd029de99f1568b4c38/libs/core/langchain_core/document_loaders/base.py#L117)
