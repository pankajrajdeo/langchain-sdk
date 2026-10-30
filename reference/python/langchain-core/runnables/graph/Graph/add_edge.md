---
title: "add_edge"
description: "Add an edge to the graph and return it."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/add_edge"
category: "reference"
tags: [reference, langchain-core, runnables, graph, add_edge]
---

# add_edge

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/add_edge)

Add an edge to the graph and return it.

## Signature

```python
add_edge(
    self,
    source: Node,
    target: Node,
    data: Stringifiable | None = None,
    conditional: bool = False,
) -> Edge
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `source` | `Node` | Yes | The source node of the edge. |
| `target` | `Node` | Yes | The target node of the edge. |
| `data` | `Stringifiable \| None` | No | Optional data associated with the edge. (default: `None`) |
| `conditional` | `bool` | No | Whether the edge is conditional. (default: `False`) |

## Returns

`Edge`

The edge that was added to the graph.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/runnables/graph.py#L356)
