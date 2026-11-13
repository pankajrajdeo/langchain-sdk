---
title: "nodes"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langgraph/pregel/main/Pregel/nodes"
category: "reference"
tags: [reference, langgraph, pregel, main, nodes]
---

# nodes

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/main/Pregel/nodes)

## Signature

```python
nodes: dict[str, PregelNode] = {k: v.build() if isinstance(v, NodeBuilder) else v for k, v in nodes.items()}
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a054ed08dcee7ecc4105706d38c0b4aa0b3c3c32/libs/langgraph/langgraph/pregel/main.py#L806)
