---
title: "UnprocessableEntityError"
description: "- APIStatusError"
source: "https://reference.langchain.com/python/langgraph-sdk/errors/UnprocessableEntityError"
category: "reference"
tags: [reference, langgraph-sdk, errors, unprocessableentityerror]
---

# UnprocessableEntityError

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/errors/UnprocessableEntityError)

## Signature

```python
UnprocessableEntityError(
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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/6b83b9b019c9b2680e4456dd6835d0fea27b9887/libs/sdk-py/langgraph_sdk/errors.py#L128)
