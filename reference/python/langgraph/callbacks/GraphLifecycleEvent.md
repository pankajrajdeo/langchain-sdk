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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/callbacks.py#L79)
