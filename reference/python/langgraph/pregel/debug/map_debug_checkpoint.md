---
title: "map_debug_checkpoint"
description: "Produce \"checkpoint\" events for stream_mode=debug."
source: "https://reference.langchain.com/python/langgraph/pregel/debug/map_debug_checkpoint"
category: "reference"
tags: [reference, langgraph, pregel, debug, map_debug_checkpoint]
---

# map_debug_checkpoint

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/debug/map_debug_checkpoint)

Produce "checkpoint" events for stream_mode=debug.

## Signature

```python
map_debug_checkpoint(
    config: RunnableConfig,
    channels: Mapping[str, BaseChannel],
    stream_channels: str | Sequence[str],
    metadata: CheckpointMetadata,
    tasks: Iterable[PregelExecutableTask],
    pending_writes: list[PendingWrite],
    parent_config: RunnableConfig | None,
    output_keys: str | Sequence[str],
) -> Iterator[CheckpointPayload]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93/libs/langgraph/langgraph/pregel/debug.py#L147)
