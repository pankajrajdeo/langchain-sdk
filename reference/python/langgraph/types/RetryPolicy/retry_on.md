---
title: "retry_on"
description: "List of exception classes that should trigger a retry, or a callable that returns True for exceptions that should trigger a retry."
source: "https://reference.langchain.com/python/langgraph/types/RetryPolicy/retry_on"
category: "reference"
tags: [reference, langgraph, types, retrypolicy, retry_on]
---

# retry_on

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/RetryPolicy/retry_on)

List of exception classes that should trigger a retry, or a callable that returns `True` for exceptions that should trigger a retry.

## Signature

```python
retry_on: type[Exception] | Sequence[type[Exception]] | Callable[[Exception], bool] = default_retry_on
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/58a6e1cc5b7dfc3619fc6e7e7573b040d554649b/libs/langgraph/langgraph/types.py#L444)
