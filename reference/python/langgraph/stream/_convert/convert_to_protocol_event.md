---
title: "convert_to_protocol_event"
description: "Convert a v2 StreamPart to a ProtocolEvent."
source: "https://reference.langchain.com/python/langgraph/stream/_convert/convert_to_protocol_event"
category: "reference"
tags: [reference, langgraph, stream, convert, convert_to_protocol_event]
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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/08a2016953789a4f579b4d36bd1967941ec62012/libs/langgraph/langgraph/stream/_convert.py#L10)
