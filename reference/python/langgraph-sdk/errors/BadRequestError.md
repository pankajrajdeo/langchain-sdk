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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/sdk-py/langgraph_sdk/errors.py#L108)
