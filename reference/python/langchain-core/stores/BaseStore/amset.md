---
title: "amset"
description: "Async set the values for the given keys."
source: "https://reference.langchain.com/python/langchain-core/stores/BaseStore/amset"
category: "reference"
tags: [reference, langchain-core, stores, basestore, amset]
---

# amset

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/stores/BaseStore/amset)

Async set the values for the given keys.

## Signature

```python
amset(
    self,
    key_value_pairs: Sequence[tuple[K, V]],
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key_value_pairs` | `Sequence[tuple[K, V]]` | Yes | A sequence of key-value pairs. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ea17e48f0a4336c920394fd029de99f1568b4c38/libs/core/langchain_core/stores.py#L112)
