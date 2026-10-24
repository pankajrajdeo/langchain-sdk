---
title: "tick"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langgraph/pregel/_runner/PregelRunner/tick"
category: "reference"
tags: [reference, langgraph, pregel, runner, pregelrunner, tick]
---

# tick

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_runner/PregelRunner/tick)

## Signature

```python
tick(
    self,
    tasks: Iterable[PregelExecutableTask],
    *,
    reraise: bool = True,
    timeout: float | None = None,
    retry_policy: Sequence[RetryPolicy] | None = None,
    get_waiter: Callable[[], concurrent.futures.Future[None]] | None = None,
    schedule_task: Callable[[PregelExecutableTask, int, Call | None], PregelExecutableTask | None],
) -> Iterator[None]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/pregel/_runner.py#L177)
