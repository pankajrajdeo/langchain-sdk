---
title: "APIResponseValidationError"
description: "- APIError"
source: "https://reference.langchain.com/python/langgraph-sdk/errors/APIResponseValidationError"
category: "reference"
tags: [reference, langgraph-sdk, errors, apiresponsevalidationerror]
---

# APIResponseValidationError

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/errors/APIResponseValidationError)

## Signature

```python
APIResponseValidationError(
    self,
    response: httpx.Response,
    body: object | None,
    *,
    message: str | None = None,
)
```

## Extends

- `APIError`

## Constructors

```python
__init__(
    self,
    response: httpx.Response,
    body: object | None,
    *,
    message: str | None = None,
) -> None
```

| Name | Type |
|------|------|
| `response` | `httpx.Response` |
| `body` | `object \| None` |
| `message` | `str \| None` |

## Properties

- `response`
- `status_code`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/sdk-py/langgraph_sdk/errors.py#L62)
