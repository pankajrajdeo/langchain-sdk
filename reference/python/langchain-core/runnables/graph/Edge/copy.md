---
title: "copy"
description: "Return a copy of the edge with optional new source and target nodes."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph/Edge/copy"
category: "reference"
tags: [reference, langchain-core, runnables, graph, edge, copy]
---

# copy

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph/Edge/copy)

Return a copy of the edge with optional new source and target nodes.

## Signature

```python
copy(
    self,
    *,
    source: str | None = None,
    target: str | None = None,
) -> Edge
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `source` | `str \| None` | No | The new source node id. (default: `None`) |
| `target` | `str \| None` | No | The new target node id. (default: `None`) |

## Returns

`Edge`

A copy of the edge with the new source and target nodes.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/runnables/graph.py#L80)
