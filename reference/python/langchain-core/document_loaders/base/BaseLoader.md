---
title: "BaseLoader"
description: "Interface for document loader."
source: "https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseLoader"
category: "reference"
tags: [reference, langchain-core, document_loaders, base, baseloader]
---

# BaseLoader

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseLoader)

Interface for document loader.

Implementations should implement the lazy-loading method using generators to avoid
loading all documents into memory at once.

`load` is provided just for user convenience and should not be overridden.

## Signature

```python
BaseLoader()
```

## Extends

- `ABC`

## Methods

- [`load()`](https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseLoader/load)
- [`aload()`](https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseLoader/aload)
- [`load_and_split()`](https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseLoader/load_and_split)
- [`lazy_load()`](https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseLoader/lazy_load)
- [`alazy_load()`](https://reference.langchain.com/python/langchain-core/document_loaders/base/BaseLoader/alazy_load)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/document_loaders/base.py#L26)
