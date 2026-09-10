---
title: "VectorStoreRetriever"
description: "Base Retriever class for VectorStore."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStoreRetriever"
category: "reference"
tags: [reference, langchain-core, vectorstores, base, vectorstoreretriever]
---

# VectorStoreRetriever

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStoreRetriever)

Base Retriever class for VectorStore.

## Signature

```python
VectorStoreRetriever(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `BaseRetriever`

## Properties

- `vectorstore`
- `search_type`
- `search_kwargs`
- `allowed_search_types`
- `model_config`

## Methods

- [`validate_search_type()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStoreRetriever/validate_search_type)
- [`add_documents()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStoreRetriever/add_documents)
- [`aadd_documents()`](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStoreRetriever/aadd_documents)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/vectorstores/base.py#L964)
