---
title: "retry_exception_types"
description: "The exception types to retry on, or a callable that receives the raised exception and returns whether to retry it. By default all exceptions are retried."
source: "https://reference.langchain.com/python/langchain-core/runnables/retry/RunnableRetry/retry_exception_types"
category: "reference"
tags: [reference, langchain-core, runnables, retry, runnableretry, retry_exception_types]
---

# retry_exception_types

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/retry/RunnableRetry/retry_exception_types)

The exception types to retry on, or a callable that receives the raised
exception and returns whether to retry it. By default all exceptions are retried.

In general you should only retry on exceptions that are likely to be
transient, such as network errors.

Good exceptions to retry are all server errors (5xx) and selected client
errors (4xx) such as 429 Too Many Requests.

## Signature

```python
retry_exception_types: tuple[type[BaseException], ...] | Callable[[BaseException], bool] = (Exception,)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/bdf0f53ed0aec3c9ae371a549e1a4d2ee4e9f021/libs/core/langchain_core/runnables/retry.py#L116)
