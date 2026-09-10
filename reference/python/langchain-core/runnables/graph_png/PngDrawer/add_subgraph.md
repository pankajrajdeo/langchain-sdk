---
title: "add_subgraph"
description: "Add subgraphs to the graph."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph_png/PngDrawer/add_subgraph"
category: "reference"
tags: [reference, langchain-core, runnables, graph_png, pngdrawer, add_subgraph]
---

# add_subgraph

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph_png/PngDrawer/add_subgraph)

Add subgraphs to the graph.

## Signature

```python
add_subgraph(
    self,
    viz: Any,
    nodes: list[list[str]],
    parent_prefix: list[str] | None = None,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `viz` | `Any` | Yes | The graphviz object. |
| `nodes` | `list[list[str]]` | Yes | The nodes to add. |
| `parent_prefix` | `list[str] \| None` | No | The prefix of the parent subgraph. (default: `None`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/graph_png.py#L166)
