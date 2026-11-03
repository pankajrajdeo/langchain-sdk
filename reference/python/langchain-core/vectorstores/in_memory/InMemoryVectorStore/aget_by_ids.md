---
title: "aget_by_ids"
description: "Async get documents by their ids."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/aget_by_ids"
category: "reference"
tags: [reference, langchain-core, vectorstores, in_memory, inmemoryvectorstore, aget_by_ids]
---

# aget_by_ids

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/aget_by_ids)

Async get documents by their ids.

## Signature

```python
aget_by_ids(
    self,
    ids: Sequence[str],
    /,
) -> list[Document]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `ids` | `Sequence[str]` | Yes | The IDs of the documents to get. |

## Returns

`list[Document]`

A list of `Document` objects.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/e936943647fe9bd9c4c24122ee3e1812ead82130/libs/core/langchain_core/vectorstores/in_memory.py#L279)
