---
title: "checkpoint"
description: "Return stored representation: always MISSING."
source: "https://reference.langchain.com/python/langgraph/channels/delta/DeltaChannel/checkpoint"
category: "reference"
tags: [reference, langgraph, channels, delta, deltachannel, checkpoint]
---

# checkpoint

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/channels/delta/DeltaChannel/checkpoint)

Return stored representation: always `MISSING`.

Snapshot decisions live in `create_checkpoint` (which has the channel
version) and write `_DeltaSnapshot(ch.get())` directly into
`channel_values`. For non-snapshot steps the channel does not appear
in `channel_values`; reconstruction walks ancestor writes via the
saver's `get_delta_channel_history`.

## Signature

```python
checkpoint(
    self,
) -> Any
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/channels/delta.py#L193)
