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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/sdk-py/langgraph_sdk/errors.py#L103)
