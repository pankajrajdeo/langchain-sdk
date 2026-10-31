---
title: "achannels_from_checkpoint"
description: "Async version of channels_from_checkpoint. See docstring there."
source: "https://reference.langchain.com/python/langgraph/pregel/main/achannels_from_checkpoint"
category: "reference"
tags: [reference, langgraph, pregel, main, achannels_from_checkpoint]
---

# achannels_from_checkpoint

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_checkpoint/achannels_from_checkpoint)

Async version of `channels_from_checkpoint`. See docstring there.

## Signature

```python
achannels_from_checkpoint(
    specs: Mapping[str, BaseChannel | ManagedValueSpec],
    checkpoint: Checkpoint,
    *,
    saver: BaseCheckpointSaver | None = None,
    config: RunnableConfig | None = None,
) -> tuple[Mapping[str, BaseChannel], ManagedValueMapping]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/pregel/_checkpoint.py#L502)
