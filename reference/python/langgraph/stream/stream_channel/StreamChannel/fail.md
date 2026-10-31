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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/stream/stream_channel.py#L146)
