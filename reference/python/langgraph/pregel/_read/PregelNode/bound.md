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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/08a2016953789a4f579b4d36bd1967941ec62012/libs/langgraph/langgraph/pregel/_read.py#L175)
