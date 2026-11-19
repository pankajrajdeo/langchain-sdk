---
title: "fail"
description: "Mark the channel as errored."
source: "https://reference.langchain.com/python/langgraph/stream/stream_channel/StreamChannel/fail"
category: "reference"
tags: [reference, langgraph, stream, stream_channel, streamchannel, fail]
---

# fail

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/stream_channel/StreamChannel/fail)

Mark the channel as errored.

## Signature

```python
fail(
    self,
    err: BaseException,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `err` | `BaseException` | Yes | The exception to surface to the subscriber. |

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93/libs/langgraph/langgraph/stream/stream_channel.py#L146)
