---
title: "copy"
description: "Return a copy of the node with optional new id and name."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph/Node/copy"
category: "reference"
tags: [reference, langchain-core, runnables, graph, node, copy]
---

# copy

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph/Node/copy)

Return a copy of the node with optional new id and name.

## Signature

```python
copy(
    self,
    *,
    id: str | None = None,
    name: str | None = None,
) -> Node
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | `str \| None` | No | The new node id. (default: `None`) |
| `name` | `str \| None` | No | The new node name. (default: `None`) |

## Returns

`Node`

A copy of the node with the new id and name.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/b4aa7e7d00c452251720ce30b8bc2c41ca44e1f5/libs/core/langchain_core/runnables/graph.py#L110)
