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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/b4aa7e7d00c452251720ce30b8bc2c41ca44e1f5/libs/core/langchain_core/stores.py#L226)
