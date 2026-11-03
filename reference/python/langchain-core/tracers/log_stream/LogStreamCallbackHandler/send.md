---
title: "send"
description: "Send a patch to the stream, return False if the stream is closed."
source: "https://reference.langchain.com/python/langchain-core/tracers/log_stream/LogStreamCallbackHandler/send"
category: "reference"
tags: [reference, langchain-core, tracers, log_stream, logstreamcallbackhandler, send]
---

# send

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/log_stream/LogStreamCallbackHandler/send)

Send a patch to the stream, return `False` if the stream is closed.

## Signature

```python
send(
    self,
    ops: dict[str, Any] = (),
) -> bool
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `*ops` | `dict[str, Any]` | No | The operations to send to the stream. (default: `()`) |

## Returns

`bool`

`True` if the patch was sent successfully, `False` if the stream is closed.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/e936943647fe9bd9c4c24122ee3e1812ead82130/libs/core/langchain_core/tracers/log_stream.py#L306)
