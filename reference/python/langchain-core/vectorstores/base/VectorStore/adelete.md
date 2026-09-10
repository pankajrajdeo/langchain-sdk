---
title: "adelete"
description: "Async delete by vector ID or other criteria."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/adelete"
category: "reference"
tags: [reference, langchain-core, vectorstores, base, vectorstore, adelete]
---

# adelete

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/adelete)

Async delete by vector ID or other criteria.

## Signature

```python
adelete(
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/vectorstores/base.py#L172)
