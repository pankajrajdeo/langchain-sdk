---
title: "set_entry_point"
description: "Specifies the first node to be called in the graph."
source: "https://reference.langchain.com/python/langgraph/graph/state/StateGraph/set_entry_point"
category: "reference"
tags: [reference, langgraph, graph, state, stategraph, set_entry_point]
---

# set_entry_point

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/graph/state/StateGraph/set_entry_point)

Specifies the first node to be called in the graph.

Equivalent to calling `add_edge(START, key)`.

## Signature

```python
set_entry_point(
    self,
    key: str,
) -> Self
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | `str` | Yes | The key of the node to set as the entry point. |

## Returns

`Self`

The instance of the graph, allowing for method chaining.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/graph/state.py#L1079)
