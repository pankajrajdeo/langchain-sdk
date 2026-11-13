---
title: "aget_subgraphs"
description: "Get the subgraphs of the graph."
source: "https://reference.langchain.com/python/langgraph/pregel/main/Pregel/aget_subgraphs"
category: "reference"
tags: [reference, langgraph, pregel, main, aget_subgraphs]
---

# aget_subgraphs

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/main/Pregel/aget_subgraphs)

Get the subgraphs of the graph.

## Signature

```python
aget_subgraphs(
    self,
    *,
    namespace: str | None = None,
    recurse: bool = False,
) -> AsyncIterator[tuple[str, PregelProtocol]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `namespace` | `str \| None` | No | Yield only the subgraph at this exact namespace, such as `parent\|child` (without task IDs). A nested namespace needs `recurse=True`. (default: `None`) |
| `recurse` | `bool` | No | Whether to recurse into the subgraphs. If `False`, only the immediate subgraphs will be returned. (default: `False`) |

## Returns

`AsyncIterator[tuple[str, PregelProtocol]]`

An iterator of the `(namespace, subgraph)` pairs.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a054ed08dcee7ecc4105706d38c0b4aa0b3c3c32/libs/langgraph/langgraph/pregel/main.py#L1196)
