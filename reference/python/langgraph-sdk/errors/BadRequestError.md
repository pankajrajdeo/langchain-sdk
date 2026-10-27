---
title: "BadRequestError"
description: "- APIStatusError"
source: "https://reference.langchain.com/python/langgraph-sdk/errors/BadRequestError"
category: "reference"
tags: [reference, langgraph-sdk, errors, badrequesterror]
---

# BadRequestError

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/errors/BadRequestError)

## Signature

```python
BadRequestError(
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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/sdk-py/langgraph_sdk/errors.py#L108)
