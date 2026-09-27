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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/pregel/debug.py#L106)
