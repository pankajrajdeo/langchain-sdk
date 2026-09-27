---
title: "GraphLifecycleEvent"
description: "Type Alias in langgraph"
source: "https://reference.langchain.com/python/langgraph/callbacks/GraphLifecycleEvent"
category: "reference"
tags: [reference, langgraph, callbacks, graphlifecycleevent]
---

# GraphLifecycleEvent

> **Type Alias** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/callbacks/GraphLifecycleEvent)

Union of all public graph lifecycle callback event payloads.

Use this alias when a callback or helper can receive either interrupt or resume
lifecycle events.

## Signature

```python
GraphLifecycleEvent: TypeAlias = GraphInterruptEvent | GraphResumeEvent
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/callbacks.py#L79)
