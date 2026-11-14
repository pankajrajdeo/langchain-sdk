---
title: "get_subgraphs"
description: "Get the subgraphs of the graph."
source: "https://reference.langchain.com/python/langgraph/pregel/main/Pregel/get_subgraphs"
category: "reference"
tags: [reference, langgraph, pregel, main, get_subgraphs]
---

# get_subgraphs

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/main/Pregel/get_subgraphs)

Get the subgraphs of the graph.

## Signature

```python
get_subgraphs(
    self,
    *,
    namespace: str | None = None,
    recurse: bool = False,
) -> Iterator[tuple[str, PregelProtocol]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `namespace` | `str \| None` | No | Yield only the subgraph at this exact namespace, such as `parent\|child` (without task IDs). A nested namespace needs `recurse=True`. (default: `None`) |
| `recurse` | `bool` | No | Whether to recurse into the subgraphs. If `False`, only the immediate subgraphs will be returned. (default: `False`) |

## Returns

`Iterator[tuple[str, PregelProtocol]]`

An iterator of the `(namespace, subgraph)` pairs.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/08a2016953789a4f579b4d36bd1967941ec62012/libs/langgraph/langgraph/pregel/main.py#L1154)
