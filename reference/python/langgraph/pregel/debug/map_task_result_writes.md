---
title: "map_task_result_writes"
description: "Folds task writes into a result dict and aggregates multiple writes to the same channel."
source: "https://reference.langchain.com/python/langgraph/pregel/debug/map_task_result_writes"
category: "reference"
tags: [reference, langgraph, pregel, debug, map_task_result_writes]
---

# map_task_result_writes

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/debug/map_task_result_writes)

Folds task writes into a result dict and aggregates multiple writes to the same channel.

If the channel contains a single write, we record the write in the result dict as `{channel: write}`
If the channel contains multiple writes, we record the writes in the result dict as `{channel: {'$writes': [write1, write2, ...]}}`

## Signature

```python
map_task_result_writes(
    writes: Sequence[tuple[str, Any]],
) -> dict[str, Any]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/pregel/debug.py#L86)
