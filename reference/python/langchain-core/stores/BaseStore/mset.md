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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/bdf0f53ed0aec3c9ae371a549e1a4d2ee4e9f021/libs/core/langchain_core/stores.py#L104)
