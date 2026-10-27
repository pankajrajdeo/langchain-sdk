---
title: "Durability"
description: "Durability mode for the graph execution."
source: "https://reference.langchain.com/python/langgraph/types/Durability"
category: "reference"
tags: [reference, langgraph, types, durability]
---

# Durability

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/Durability)

Durability mode for the graph execution.

- `'sync'`: Changes are persisted synchronously before the next step starts.
- `'async'`: Changes are persisted asynchronously while the next step executes.
- `'exit'`: Changes are persisted only when the graph exits.

## Signature

```python
Durability = Literal['sync', 'async', 'exit']
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/langgraph/langgraph/types.py#L98)
