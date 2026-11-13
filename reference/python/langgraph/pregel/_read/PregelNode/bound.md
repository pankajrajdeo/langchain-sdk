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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a054ed08dcee7ecc4105706d38c0b4aa0b3c3c32/libs/langgraph/langgraph/pregel/_read.py#L175)
