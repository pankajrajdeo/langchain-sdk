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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/callbacks.py#L79)
