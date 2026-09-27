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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/types.py#L443)
