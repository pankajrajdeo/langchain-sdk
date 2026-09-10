---
title: "upsert"
description: "Upsert documents into the index."
source: "https://reference.langchain.com/python/langchain-core/indexing/in_memory/InMemoryDocumentIndex/upsert"
category: "reference"
tags: [reference, langchain-core, indexing, in_memory, inmemorydocumentindex, upsert]
---

# upsert

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/indexing/in_memory/InMemoryDocumentIndex/upsert)

Upsert documents into the index.

## Signature

```python
upsert(
    self,
    items: Sequence[Document],
    /,
    **kwargs: Any = {},
) -> UpsertResponse
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `items` | `Sequence[Document]` | Yes | Sequence of documents to add to the index. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

## Returns

`UpsertResponse`

A response object that contains the list of IDs that were

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/indexing/in_memory.py#L31)
