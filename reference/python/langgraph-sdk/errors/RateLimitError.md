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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5db97b9ccab6b8d9a5ab1e8f0bebea7c03a8708a/libs/sdk-py/langgraph_sdk/errors.py#L132)
