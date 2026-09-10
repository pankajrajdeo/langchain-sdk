---
title: "delete"
description: "Delete by IDs or other criteria."
source: "https://reference.langchain.com/python/langchain-core/indexing/base/DocumentIndex/delete"
category: "reference"
tags: [reference, langchain-core, indexing, base, documentindex, delete]
---

# delete

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/indexing/base/DocumentIndex/delete)

Delete by IDs or other criteria.

Calling delete without any input parameters should raise a ValueError!

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
| `**kwargs` | `Any` | No | Additional keyword arguments. This is up to the implementation. For example, can include an option to delete the entire index, or else issue a non-blocking delete etc. (default: `{}`) |

## Returns

`DeleteResponse`

A response object that contains the list of IDs that were

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/indexing/base.py#L564)
