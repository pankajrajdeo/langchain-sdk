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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/sdk-py/langgraph_sdk/stream/subscription.py#L68)
