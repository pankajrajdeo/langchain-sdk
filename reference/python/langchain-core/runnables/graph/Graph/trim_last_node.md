---
title: "trim_last_node"
description: "Remove the last node if it exists and has a single incoming edge."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/trim_last_node"
category: "reference"
tags: [reference, langchain-core, runnables, graph, trim_last_node]
---

# trim_last_node

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/trim_last_node)

Remove the last node if it exists and has a single incoming edge.

i.e., if removing it would not leave the graph without a "last" node.

## Signature

```python
trim_last_node(
    self,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/graph.py#L496)
