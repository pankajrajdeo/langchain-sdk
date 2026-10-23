---
title: "node_data_str"
description: "Convert the data of a node to a string."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph/node_data_str"
category: "reference"
tags: [reference, langchain-core, runnables, graph, node_data_str]
---

# node_data_str

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph/node_data_str)

Convert the data of a node to a string.

## Signature

```python
node_data_str(
    id: str,
    data: TypeBaseModel | RunnableType[Any, Any] | None,
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | `str` | Yes | The node id. |
| `data` | `TypeBaseModel \| RunnableType[Any, Any] \| None` | Yes | The node data. |

## Returns

`str`

A string representation of the data.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/runnables/graph.py#L180)
