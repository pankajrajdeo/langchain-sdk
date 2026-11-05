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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/_internal/_replay.py#L75)
