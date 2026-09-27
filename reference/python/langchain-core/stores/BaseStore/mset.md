---
title: "mset"
description: "Set the values for the given keys."
source: "https://reference.langchain.com/python/langchain-core/stores/BaseStore/mset"
category: "reference"
tags: [reference, langchain-core, stores, basestore, mset]
---

# mset

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/stores/BaseStore/mset)

Set the values for the given keys.

## Signature

```python
mset(
    self,
    key_value_pairs: Sequence[tuple[K, V]],
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key_value_pairs` | `Sequence[tuple[K, V]]` | Yes | A sequence of key-value pairs. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/stores.py#L104)
