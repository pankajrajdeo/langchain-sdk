---
title: "aget_checkpoint"
description: "Async version of get_checkpoint."
source: "https://reference.langchain.com/python/langgraph/_internal/_replay/ReplayState/aget_checkpoint"
category: "reference"
tags: [reference, langgraph, internal, replay, replaystate, aget_checkpoint]
---

# aget_checkpoint

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_replay/ReplayState/aget_checkpoint)

Async version of `get_checkpoint`.

## Signature

```python
aget_checkpoint(
    self,
    checkpoint_ns: str,
    checkpointer: BaseCheckpointSaver,
    checkpoint_config: RunnableConfig,
) -> CheckpointTuple | None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/_internal/_replay.py#L75)
