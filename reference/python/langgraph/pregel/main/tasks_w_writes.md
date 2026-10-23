---
title: "tasks_w_writes"
description: "Apply writes / subgraph states to tasks to be returned in a StateSnapshot."
source: "https://reference.langchain.com/python/langgraph/pregel/main/tasks_w_writes"
category: "reference"
tags: [reference, langgraph, pregel, main, tasks_w_writes]
---

# tasks_w_writes

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/debug/tasks_w_writes)

Apply writes / subgraph states to tasks to be returned in a StateSnapshot.

With `live=True`, tasks report only the interrupts still waiting for an
answer, as of the most recent writes. Otherwise tasks report the interrupts
they raised in the step, including answered ones, as a record of the step.

## Signature

```python
tasks_w_writes(
    tasks: Iterable[PregelTask | PregelExecutableTask],
    pending_writes: list[PendingWrite] | None,
    states: dict[str, RunnableConfig | StateSnapshot] | None,
    output_keys: str | Sequence[str],
    *,
    live: bool = False,
) -> tuple[PregelTask, ...]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/pregel/debug.py#L212)
