---
title: "cache_set"
description: "Set a value in the cache."
source: "https://reference.langchain.com/python/langgraph-sdk/cache/cache_set"
category: "reference"
tags: [reference, langgraph-sdk, cache, cache_set]
---

# cache_set

> **Function** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/cache/cache_set)

Set a value in the cache.

## Signature

```python
cache_set(
    key: str,
    value: Any,
    *,
    ttl: timedelta | None = None,
) -> None
```

## Description

Requires Agent Server runtime version 0.7.29 or later.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | `str` | Yes | The cache key. |
| `value` | `Any` | Yes | The value to cache (must be JSON-serializable). |
| `ttl` | `timedelta \| None` | No | Optional time-to-live. Capped at 1 day; ``None`` or zero defaults to 1 day. (default: `None`) |

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/sdk-py/langgraph_sdk/cache.py#L74)
