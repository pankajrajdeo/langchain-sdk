---
title: "GraphLifecycleStatus"
description: "Type Alias in langgraph"
source: "https://reference.langchain.com/python/langgraph/callbacks/GraphLifecycleStatus"
category: "reference"
tags: [reference, langgraph, callbacks, graphlifecyclestatus]
---

# GraphLifecycleStatus

> **Type Alias** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/callbacks/GraphLifecycleStatus)

Allowed lifecycle statuses reported in graph lifecycle callback events.

## Signature

```python
GraphLifecycleStatus: TypeAlias = Literal['input', 'pending', 'done', 'interrupt_before', 'interrupt_after', 'out_of_steps']
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/callbacks.py#L31)
