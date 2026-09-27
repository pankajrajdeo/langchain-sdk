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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/pregel/_runner.py#L176)
