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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a054ed08dcee7ecc4105706d38c0b4aa0b3c3c32/libs/langgraph/langgraph/pregel/debug.py#L147)
