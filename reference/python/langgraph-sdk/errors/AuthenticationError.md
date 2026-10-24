---
title: "AuthenticationError"
description: "- APIStatusError"
source: "https://reference.langchain.com/python/langgraph-sdk/errors/AuthenticationError"
category: "reference"
tags: [reference, langgraph-sdk, errors, authenticationerror]
---

# AuthenticationError

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/errors/AuthenticationError)

## Signature

```python
AuthenticationError(
    self,
    message: str,
    *,
    response: httpx.Response,
    body: object | None,
)
```

## Extends

- `APIStatusError`

## Properties

- `status_code`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/6b83b9b019c9b2680e4456dd6835d0fea27b9887/libs/sdk-py/langgraph_sdk/errors.py#L112)
