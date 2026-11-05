---
title: "RateLimitError"
description: "- APIStatusError"
source: "https://reference.langchain.com/python/langgraph-sdk/errors/RateLimitError"
category: "reference"
tags: [reference, langgraph-sdk, errors, ratelimiterror]
---

# RateLimitError

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/errors/RateLimitError)

## Signature

```python
RateLimitError(
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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/sdk-py/langgraph_sdk/errors.py#L132)
