---
title: "acquire"
description: "Attempt to acquire the necessary tokens for the rate limiter."
source: "https://reference.langchain.com/python/langchain-core/rate_limiters/BaseRateLimiter/acquire"
category: "reference"
tags: [reference, langchain-core, rate_limiters, baseratelimiter, acquire]
---

# acquire

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/rate_limiters/BaseRateLimiter/acquire)

Attempt to acquire the necessary tokens for the rate limiter.

This method blocks until the required tokens are available if `blocking`
is set to `True`.

If `blocking` is set to `False`, the method will immediately return the result
of the attempt to acquire the tokens.

## Signature

```python
acquire(
    self,
    *,
    blocking: bool = True,
) -> bool
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `blocking` | `bool` | No | If `True`, the method will block until the tokens are available. If `False`, the method will return immediately with the result of the attempt. (default: `True`) |

## Returns

`bool`

`True` if the tokens were successfully acquired, `False` otherwise.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/rate_limiters.py#L28)
