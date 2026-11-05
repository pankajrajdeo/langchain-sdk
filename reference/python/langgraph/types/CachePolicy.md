---
title: "CachePolicy"
description: "Configuration for caching nodes."
source: "https://reference.langchain.com/python/langgraph/types/CachePolicy"
category: "reference"
tags: [reference, langgraph, types, cachepolicy]
---

# CachePolicy

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/CachePolicy)

Configuration for caching nodes.

## Signature

```python
CachePolicy(
    self,
    *,
    key_func: KeyFuncT = default_cache_key,
    ttl: int | None = None,
)
```

## Extends

- `Generic[KeyFuncT]`

## Constructors

```python
__init__(
    self,
    *,
    key_func: KeyFuncT = default_cache_key,
    ttl: int | None = None,
) -> None
```

| Name | Type |
|------|------|
| `key_func` | `KeyFuncT` |
| `ttl` | `int \| None` |

## Properties

- `key_func`
- `ttl`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/types.py#L530)
