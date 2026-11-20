---
title: "ayield_keys"
description: "Async get an iterator over keys that match the given prefix."
source: "https://reference.langchain.com/python/langchain-core/stores/BaseStore/ayield_keys"
category: "reference"
tags: [reference, langchain-core, stores, basestore, ayield_keys]
---

# ayield_keys

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/stores/BaseStore/ayield_keys)

Async get an iterator over keys that match the given prefix.

## Signature

```python
ayield_keys(
    self,
    *,
    prefix: str | None = None,
) -> AsyncIterator[K] | AsyncIterator[str]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `prefix` | `str \| None` | No | The prefix to match. (default: `None`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d4dafe5839c4a6b07d71cc78697df0de9e627e21/libs/core/langchain_core/stores.py#L150)
