---
title: "trim_first_node"
description: "Remove the first node if it exists and has a single outgoing edge."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/trim_first_node"
category: "reference"
tags: [reference, langchain-core, runnables, graph, trim_first_node]
---

# trim_first_node

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/trim_first_node)

Remove the first node if it exists and has a single outgoing edge.

i.e., if removing it would not leave the graph without a "first" node.

## Signature

```python
trim_first_node(
    self,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/04ac76c07ec173a44e3e57de54861d0b637e3299/libs/core/langchain_core/runnables/graph.py#L483)
