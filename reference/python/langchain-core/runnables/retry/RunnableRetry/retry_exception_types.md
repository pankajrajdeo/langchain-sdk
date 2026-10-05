---
title: "retry_exception_types"
description: "The exception types to retry on. By default all exceptions are retried."
source: "https://reference.langchain.com/python/langchain-core/runnables/retry/RunnableRetry/retry_exception_types"
category: "reference"
tags: [reference, langchain-core, runnables, retry, runnableretry, retry_exception_types]
---

# retry_exception_types

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/retry/RunnableRetry/retry_exception_types)

The exception types to retry on. By default all exceptions are retried.

In general you should only retry on exceptions that are likely to be
transient, such as network errors.

Good exceptions to retry are all server errors (5xx) and selected client
errors (4xx) such as 429 Too Many Requests.

## Signature

```python
retry_exception_types: tuple[type[BaseException], ...] = (Exception,)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/04ac76c07ec173a44e3e57de54861d0b637e3299/libs/core/langchain_core/runnables/retry.py#L114)
