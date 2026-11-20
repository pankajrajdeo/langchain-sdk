---
title: "bound"
description: "The main logic of the node. This will be invoked with the input from channels."
source: "https://reference.langchain.com/python/langgraph/pregel/_read/PregelNode/bound"
category: "reference"
tags: [reference, langgraph, pregel, read, pregelnode, bound]
---

# bound

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_read/PregelNode/bound)

The main logic of the node. This will be invoked with the input from 
`channels`.

## Signature

```python
bound: Runnable[Any, Any] = bound if bound is not None else DEFAULT_BOUND
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/58a6e1cc5b7dfc3619fc6e7e7573b040d554649b/libs/langgraph/langgraph/pregel/_read.py#L175)
