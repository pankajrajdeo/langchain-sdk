---
title: "exit_delta_task_id"
description: "Synthetic task id for exit-mode DeltaChannel writes."
source: "https://reference.langchain.com/python/langgraph/pregel/_checkpoint/exit_delta_task_id"
category: "reference"
tags: [reference, langgraph, pregel, checkpoint, exit_delta_task_id]
---

# exit_delta_task_id

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_checkpoint/exit_delta_task_id)

Synthetic task id for exit-mode DeltaChannel writes.

Embeds the superstep in the first UUID group so `ORDER BY task_id, idx`
preserves chronological order while remaining a valid RFC UUID (required by
Postgres `checkpoint_writes.task_id uuid` columns).

## Signature

```python
exit_delta_task_id(
    step: int,
    task_id: str,
) -> str
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/pregel/_checkpoint.py#L39)
