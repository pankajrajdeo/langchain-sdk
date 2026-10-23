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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/pregel/debug.py#L86)
