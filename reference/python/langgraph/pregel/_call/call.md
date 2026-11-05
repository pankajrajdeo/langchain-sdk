---
title: "call"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langgraph/pregel/_call/call"
category: "reference"
tags: [reference, langgraph, pregel, call]
---

# call

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_call/call)

## Signature

```python
call(
    func: Callable[P, Awaitable[T]] | Callable[P, T],
    args: Any = (),
    *,
    retry_policy: Sequence[RetryPolicy] | None = None,
    cache_policy: CachePolicy | None = None,
    timeout: float | timedelta | TimeoutPolicy | None = None,
    kwargs: Any = {},
) -> SyncAsyncFuture[T]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/pregel/_call.py#L258)
