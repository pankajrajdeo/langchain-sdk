---
title: "map_debug_task_results"
description: "Produce \"task_result\" events for stream_mode=debug."
source: "https://reference.langchain.com/python/langgraph/pregel/debug/map_debug_task_results"
category: "reference"
tags: [reference, langgraph, pregel, debug, map_debug_task_results]
---

# map_debug_task_results

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/debug/map_debug_task_results)

Produce "task_result" events for stream_mode=debug.

## Signature

```python
map_debug_task_results(
    task_tup: tuple[PregelExecutableTask, Sequence[tuple[str, Any]]],
    stream_keys: str | Sequence[str],
) -> Iterator[TaskResultPayload]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/58a6e1cc5b7dfc3619fc6e7e7573b040d554649b/libs/langgraph/langgraph/pregel/debug.py#L109)
