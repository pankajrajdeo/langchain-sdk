---
title: "RetryOn"
description: "Type Alias in langchain"
source: "https://reference.langchain.com/python/langchain/agents/middleware/_retry/RetryOn"
category: "reference"
tags: [reference, langchain, agents, middleware, retry, retryon]
---

# RetryOn

> **Type Alias** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/_retry/RetryOn)

Type for specifying which exceptions to retry on.

Can be either:
- A tuple of exception types to retry on (based on `isinstance` checks)
- A callable that takes an exception and returns `True` if it should be retried

## Signature

```python
RetryOn = tuple[type[Exception], ...] | Callable[[Exception], bool]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/5dcec1858191a6b54cd843dd8e54d856e2e007cc/libs/langchain_v1/langchain/agents/middleware/_retry.py#L16)
