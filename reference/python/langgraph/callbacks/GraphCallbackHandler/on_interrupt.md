---
title: "on_interrupt"
description: "Run when graph execution pauses due to one or more interrupts."
source: "https://reference.langchain.com/python/langgraph/callbacks/GraphCallbackHandler/on_interrupt"
category: "reference"
tags: [reference, langgraph, callbacks, graphcallbackhandler, on_interrupt]
---

# on_interrupt

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/callbacks/GraphCallbackHandler/on_interrupt)

Run when graph execution pauses due to one or more interrupts.

## Signature

```python
on_interrupt(
    self,
    event: GraphInterruptEvent,
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `event` | `GraphInterruptEvent` | Yes | Interrupt lifecycle event payload. |

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93/libs/langgraph/langgraph/callbacks.py#L99)
