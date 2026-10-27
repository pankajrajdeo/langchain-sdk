---
title: "ThreadTTL"
description: "Time-to-live configuration for a thread."
source: "https://reference.langchain.com/python/langgraph-sdk/auth/types/ThreadTTL"
category: "reference"
tags: [reference, langgraph-sdk, auth, types, threadttl]
---

# ThreadTTL

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/auth/types/ThreadTTL)

Time-to-live configuration for a thread.

Matches the OpenAPI schema where TTL is represented as an object with
an optional strategy and a time value in minutes.

## Signature

```python
ThreadTTL()
```

## Extends

- `typing.TypedDict`

## Constructors

```python
__init__(
    strategy: typing.Literal['delete'],
    ttl: int,
)
```

| Name | Type |
|------|------|
| `strategy` | `typing.Literal['delete']` |
| `ttl` | `int` |

## Properties

- `strategy`
- `ttl`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/sdk-py/langgraph_sdk/auth/types.py#L429)
