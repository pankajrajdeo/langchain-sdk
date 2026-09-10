---
title: "last_node"
description: "Find the single node that is not a source of any edge."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/last_node"
category: "reference"
tags: [reference, langchain-core, runnables, graph, last_node]
---

# last_node

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/last_node)

Find the single node that is not a source of any edge.

If there is no such node, or there are multiple, return `None`.
When drawing the graph, this node would be the destination.

## Signature

```python
last_node(
    self,
) -> Node | None
```

## Returns

`Node | None`

The last node, or None if there is no such node or multiple

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/graph.py#L471)
