---
title: "atick"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langgraph/pregel/_runner/PregelRunner/atick"
category: "reference"
tags: [reference, langgraph, pregel, runner, pregelrunner, atick]
---

# atick

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_runner/PregelRunner/atick)

## Signature

```python
atick(
    self,
    tasks: Iterable[PregelExecutableTask],
    *,
    reraise: bool = True,
    timeout: float | None = None,
    retry_policy: Sequence[RetryPolicy] | None = None,
    get_waiter: Callable[[], asyncio.Future[None]] | None = None,
    schedule_task: Callable[[PregelExecutableTask, int, Call | None], Awaitable[PregelExecutableTask | None]],
) -> AsyncIterator[None]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/pregel/_runner.py#L361)
