---
title: "amdelete"
description: "Async delete the given keys and their associated values."
source: "https://reference.langchain.com/python/langchain-core/stores/BaseStore/amdelete"
category: "reference"
tags: [reference, langchain-core, stores, basestore, amdelete]
---

# amdelete

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/stores/BaseStore/amdelete)

Async delete the given keys and their associated values.

## Signature

```python
amdelete(
    self,
    keys: Sequence[K],
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `keys` | `Sequence[K]` | Yes | A sequence of keys to delete. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/stores.py#L128)
