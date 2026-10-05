---
title: "delete"
description: "Delete by vector ID or other criteria."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/delete"
category: "reference"
tags: [reference, langchain-core, vectorstores, base, vectorstore, delete]
---

# delete

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/delete)

Delete by vector ID or other criteria.

## Signature

```python
delete(
    self,
    ids: list[str] | None = None,
    **kwargs: Any = {},
) -> bool | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `ids` | `list[str] \| None` | No | List of IDs to delete. If `None`, delete all. (default: `None`) |
| `**kwargs` | `Any` | No | Other keyword arguments that subclasses might use. (default: `{}`) |

## Returns

`bool | None`

`True` if deletion is successful, `False` otherwise, `None` if not
implemented.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/04ac76c07ec173a44e3e57de54861d0b637e3299/libs/core/langchain_core/vectorstores/base.py#L108)
