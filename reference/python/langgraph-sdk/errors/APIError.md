---
title: "APIError"
description: "- httpx.HTTPStatusError - LangGraphError"
source: "https://reference.langchain.com/python/langgraph-sdk/errors/APIError"
category: "reference"
tags: [reference, langgraph-sdk, errors, apierror]
---

# APIError

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/errors/APIError)

## Signature

```python
APIError(
    self,
    message: str,
    response_or_request: httpx.Response | httpx.Request,
    *,
    body: object | None,
)
```

## Extends

- `httpx.HTTPStatusError`
- `LangGraphError`

## Constructors

```python
__init__(
    self,
    message: str,
    response_or_request: httpx.Response | httpx.Request,
    *,
    body: object | None,
) -> None
```

| Name | Type |
|------|------|
| `message` | `str` |
| `response_or_request` | `httpx.Response \| httpx.Request` |
| `body` | `object \| None` |

## Properties

- `message`
- `request`
- `body`
- `code`
- `param`
- `type`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/sdk-py/langgraph_sdk/errors.py#L17)
