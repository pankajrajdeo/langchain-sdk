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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/types.py#L109)
