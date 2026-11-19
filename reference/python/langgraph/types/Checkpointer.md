---
title: "Checkpointer"
description: "Type Alias in langgraph"
source: "https://reference.langchain.com/python/langgraph/types/Checkpointer"
category: "reference"
tags: [reference, langgraph, types, checkpointer]
---

# Checkpointer

> **Type Alias** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/Checkpointer)

Type of the checkpointer to use for a subgraph.

- `True` enables persistent checkpointing for this subgraph.
- `False` disables checkpointing, even if the parent graph has a checkpointer.
- `None` inherits checkpointer from the parent graph.

## Signature

```python
Checkpointer = None | bool | BaseCheckpointSaver
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93/libs/langgraph/langgraph/types.py#L110)
