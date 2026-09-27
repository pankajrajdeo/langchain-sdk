---
title: "amget"
description: "Async get the values associated with the given keys."
source: "https://reference.langchain.com/python/langchain-core/stores/BaseStore/amget"
category: "reference"
tags: [reference, langchain-core, stores, basestore, amget]
---

# amget

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/stores/BaseStore/amget)

Async get the values associated with the given keys.

## Signature

```python
amget(
    self,
    keys: Sequence[K],
) -> list[V | None]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `keys` | `Sequence[K]` | Yes | A sequence of keys. |

## Returns

`list[V | None]`

A sequence of optional values associated with the keys.
If a key is not found, the corresponding value will be `None`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/stores.py#L92)
