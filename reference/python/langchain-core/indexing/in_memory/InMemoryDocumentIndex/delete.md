---
title: "delete"
description: "Delete by IDs."
source: "https://reference.langchain.com/python/langchain-core/indexing/in_memory/InMemoryDocumentIndex/delete"
category: "reference"
tags: [reference, langchain-core, indexing, in_memory, inmemorydocumentindex, delete]
---

# delete

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/indexing/in_memory/InMemoryDocumentIndex/delete)

Delete by IDs.

## Signature

```python
delete(
    self,
    ids: list[str] | None = None,
    **kwargs: Any = {},
) -> DeleteResponse
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `ids` | `list[str] \| None` | No | List of IDs to delete. (default: `None`) |

## Returns

`DeleteResponse`

A response object that contains the list of IDs that were successfully

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/indexing/in_memory.py#L60)
