---
title: "add_edge"
description: "Adds an edge to the graph."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph_png/PngDrawer/add_edge"
category: "reference"
tags: [reference, langchain-core, runnables, graph_png, pngdrawer, add_edge]
---

# add_edge

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph_png/PngDrawer/add_edge)

Adds an edge to the graph.

## Signature

```python
add_edge(
    self,
    viz: Any,
    source: str,
    target: str,
    label: str | None = None,
    conditional: bool = False,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `viz` | `Any` | Yes | The graphviz object. |
| `source` | `str` | Yes | The source node. |
| `target` | `str` | Yes | The target node. |
| `label` | `str \| None` | No | The label for the edge. (default: `None`) |
| `conditional` | `bool` | No | Whether the edge is conditional. (default: `False`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/graph_png.py#L94)
