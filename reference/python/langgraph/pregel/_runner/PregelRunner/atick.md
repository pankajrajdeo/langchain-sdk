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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/pregel/_runner.py#L361)
