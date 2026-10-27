---
title: "set_finish_point"
description: "Marks a node as a finish point of the graph."
source: "https://reference.langchain.com/python/langgraph/graph/state/StateGraph/set_finish_point"
category: "reference"
tags: [reference, langgraph, graph, state, stategraph, set_finish_point]
---

# set_finish_point

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/graph/state/StateGraph/set_finish_point)

Marks a node as a finish point of the graph.

If the graph reaches this node, it will cease execution.

## Signature

```python
set_finish_point(
    self,
    key: str,
) -> Self
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | `str` | Yes | The key of the node to set as the finish point. |

## Returns

`Self`

The instance of the graph, allowing for method chaining.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/langgraph/langgraph/graph/state.py#L1116)
