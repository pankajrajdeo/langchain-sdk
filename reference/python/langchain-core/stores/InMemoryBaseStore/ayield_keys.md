---
title: "ayield_keys"
description: "Async get an async iterator over keys that match the given prefix."
source: "https://reference.langchain.com/python/langchain-core/stores/InMemoryBaseStore/ayield_keys"
category: "reference"
tags: [reference, langchain-core, stores, inmemorybasestore, ayield_keys]
---

# ayield_keys

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/stores/InMemoryBaseStore/ayield_keys)

Async get an async iterator over keys that match the given prefix.

## Signature

```python
ayield_keys(
    self,
    *,
    prefix: str | None = None,
) -> AsyncIterator[str]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `prefix` | `str \| None` | No | The prefix to match. (default: `None`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/5069b326c53069ec85a7e1d914c6873feb8d0cfa/libs/core/langchain_core/stores.py#L226)
