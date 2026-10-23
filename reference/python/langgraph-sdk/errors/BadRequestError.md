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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/sdk-py/langgraph_sdk/errors.py#L108)
