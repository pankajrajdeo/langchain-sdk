---
title: "checkpoint"
description: "Return a serializable representation of the channel's current state."
source: "https://reference.langchain.com/python/langgraph/channels/base/BaseChannel/checkpoint"
category: "reference"
tags: [reference, langgraph, channels, base, basechannel, checkpoint]
---

# checkpoint

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/channels/base/BaseChannel/checkpoint)

Return a serializable representation of the channel's current state.

Raises `EmptyChannelError` if the channel is empty (never updated yet),
or doesn't support checkpoints.

## Signature

```python
checkpoint(
    self,
) -> Checkpoint | Any
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/channels/base.py#L49)
