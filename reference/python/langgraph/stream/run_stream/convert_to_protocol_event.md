---
title: "convert_to_protocol_event"
description: "Convert a v2 StreamPart to a ProtocolEvent."
source: "https://reference.langchain.com/python/langgraph/stream/run_stream/convert_to_protocol_event"
category: "reference"
tags: [reference, langgraph, stream, run_stream, convert_to_protocol_event]
---

# convert_to_protocol_event

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/_convert/convert_to_protocol_event)

Convert a v2 StreamPart to a ProtocolEvent.

## Signature

```python
convert_to_protocol_event(
    part: StreamPart,
) -> ProtocolEvent
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `part` | `StreamPart` | Yes | A stream part with keys `type`, `ns`, `data`, and optionally `interrupts` (present on values events). |

## Returns

`ProtocolEvent`

The equivalent ProtocolEvent.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/stream/_convert.py#L10)
