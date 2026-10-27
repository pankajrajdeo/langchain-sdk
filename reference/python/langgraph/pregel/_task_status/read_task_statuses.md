---
title: "read_task_statuses"
description: "Return the status of every task that has recorded writes, keyed by task id."
source: "https://reference.langchain.com/python/langgraph/pregel/_task_status/read_task_statuses"
category: "reference"
tags: [reference, langgraph, pregel, task_status, read_task_statuses]
---

# read_task_statuses

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_task_status/read_task_statuses)

Return the status of every task that has recorded writes, keyed by task id.

Writes from `NULL_TASK_ID` are input to the superstep, not task activity, so
they are not included.

## Signature

```python
read_task_statuses(
    pending_writes: Iterable[PendingWrite],
) -> dict[str, TaskStatus]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/langgraph/langgraph/pregel/_task_status.py#L99)
