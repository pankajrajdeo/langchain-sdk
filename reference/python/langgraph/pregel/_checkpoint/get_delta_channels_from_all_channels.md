---
title: "get_delta_channels_from_all_channels"
description: "DeltaChannels to snapshot on the first update_state of a fresh thread: the ones it wrote, as the rest have no version and nothing to store."
source: "https://reference.langchain.com/python/langgraph/pregel/_checkpoint/get_delta_channels_from_all_channels"
category: "reference"
tags: [reference, langgraph, pregel, checkpoint, get_delta_channels_from_all_channels]
---

# get_delta_channels_from_all_channels

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_checkpoint/get_delta_channels_from_all_channels)

DeltaChannels to snapshot on the first update_state of a fresh thread:
the ones it wrote, as the rest have no version and nothing to store.

## Signature

```python
get_delta_channels_from_all_channels(
    channels: Mapping[str, BaseChannel],
    channel_versions: ChannelVersions,
) -> set[str]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/pregel/_checkpoint.py#L127)
