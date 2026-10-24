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
| `namespace` | `str \| None` | No | The namespace to filter the subgraphs by. (default: `None`) |
| `recurse` | `bool` | No | Whether to recurse into the subgraphs. If `False`, only the immediate subgraphs will be returned. (default: `False`) |

## Returns

`AsyncIterator[tuple[str, PregelProtocol]]`

An iterator of the `(namespace, subgraph)` pairs.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/pregel/main.py#L1183)
