---
title: "exit_delta_late_task_id"
description: "Synthetic task id for exit-mode writes of a superstep after the anchor's own."
source: "https://reference.langchain.com/python/langgraph/pregel/_checkpoint/exit_delta_late_task_id"
category: "reference"
tags: [reference, langgraph, pregel, checkpoint, exit_delta_late_task_id]
---

# exit_delta_late_task_id

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_checkpoint/exit_delta_late_task_id)

Synthetic task id for exit-mode writes of a superstep after the anchor's own.

Sorts after every real task id, in step order, so replay keeps them after
the anchor's own superstep whether a saver orders by task path or task id.

## Signature

```python
exit_delta_late_task_id(
    step: int,
    task_id: str,
) -> str
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/pregel/_checkpoint.py#L80)
