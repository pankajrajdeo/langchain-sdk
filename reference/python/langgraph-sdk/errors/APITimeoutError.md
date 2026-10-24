---
title: "APITimeoutError"
description: "- APIConnectionError"
source: "https://reference.langchain.com/python/langgraph-sdk/errors/APITimeoutError"
category: "reference"
tags: [reference, langgraph-sdk, errors, apitimeouterror]
---

# APITimeoutError

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/errors/APITimeoutError)

## Signature

```python
APITimeoutError(
    self,
    request: httpx.Request,
)
```

## Extends

- `APIConnectionError`

## Constructors

```python
__init__(
    self,
    request: httpx.Request,
) -> None
```

| Name | Type |
|------|------|
| `request` | `httpx.Request` |

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/6b83b9b019c9b2680e4456dd6835d0fea27b9887/libs/sdk-py/langgraph_sdk/errors.py#L103)
