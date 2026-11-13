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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a054ed08dcee7ecc4105706d38c0b4aa0b3c3c32/libs/langgraph/langgraph/types.py#L99)
