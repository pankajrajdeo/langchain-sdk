---
title: "infer_channel"
description: "Map a protocol event's method to its subscription channel."
source: "https://reference.langchain.com/python/langgraph-sdk/stream/subscription/infer_channel"
category: "reference"
tags: [reference, langgraph-sdk, stream, subscription, infer_channel]
---

# infer_channel

> **Function** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/stream/subscription/infer_channel)

Map a protocol event's `method` to its subscription channel.

Returns `None` for unrecognized methods so new server-side channels (e.g.
from extension transformers) don't break existing clients.

## Signature

```python
infer_channel(
    event: Event,
) -> Channel | None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/6b83b9b019c9b2680e4456dd6835d0fea27b9887/libs/sdk-py/langgraph_sdk/stream/subscription.py#L68)
