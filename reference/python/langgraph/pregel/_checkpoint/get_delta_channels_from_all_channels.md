---
title: "get_delta_channels_from_all_channels"
description: "DeltaChannels to snapshot on the first update_state of a fresh thread."
source: "https://reference.langchain.com/python/langgraph/pregel/_checkpoint/get_delta_channels_from_all_channels"
category: "reference"
tags: [reference, langgraph, pregel, checkpoint, get_delta_channels_from_all_channels]
---

# get_delta_channels_from_all_channels

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_checkpoint/get_delta_channels_from_all_channels)

DeltaChannels to snapshot on the first update_state of a fresh thread.

## Signature

```python
get_delta_channels_from_all_channels(
    channels: Mapping[str, BaseChannel],
) -> set[str]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/pregel/_checkpoint.py#L81)
