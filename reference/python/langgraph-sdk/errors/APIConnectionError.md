---
title: "APIConnectionError"
description: "- APIError"
source: "https://reference.langchain.com/python/langgraph-sdk/errors/APIConnectionError"
category: "reference"
tags: [reference, langgraph-sdk, errors, apiconnectionerror]
---

# APIConnectionError

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/errors/APIConnectionError)

## Signature

```python
APIConnectionError(
    self,
    *,
    message: str = 'Connection error.',
    request: httpx.Request,
)
```

## Extends

- `APIError`

## Constructors

```python
__init__(
    self,
    *,
    message: str = 'Connection error.',
    request: httpx.Request,
) -> None
```

| Name | Type |
|------|------|
| `message` | `str` |
| `request` | `httpx.Request` |

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/sdk-py/langgraph_sdk/errors.py#L96)
