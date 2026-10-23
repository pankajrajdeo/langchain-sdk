---
title: "aprocess"
description: "Handle an event on the async lane."
source: "https://reference.langchain.com/python/langgraph/stream/_types/StreamTransformer/aprocess"
category: "reference"
tags: [reference, langgraph, stream, types, streamtransformer, aprocess]
---

# aprocess

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/_types/StreamTransformer/aprocess)

Handle an event on the async lane.

The mux awaits this before dispatching to the next transformer,
so a slow `aprocess` serializes the pipeline. Use it only when
a later transformer — or a consumer reading the event
synchronously — must see the result of the async work (e.g.
PII redaction that mutates `event` in place).

The default delegates to `process`, so purely-sync transformers
run unchanged under `astream()`.

## Signature

```python
aprocess(
    self,
    event: ProtocolEvent,
) -> bool
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `event` | `ProtocolEvent` | Yes | The protocol event to observe. |

## Returns

`bool`

True to keep the event in the main log, False to suppress it.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/stream/_types.py#L166)
