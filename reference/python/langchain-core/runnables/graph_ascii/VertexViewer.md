---
title: "VertexViewer"
description: "VertexViewer class."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph_ascii/VertexViewer"
category: "reference"
tags: [reference, langchain-core, runnables, graph_ascii, vertexviewer]
---

# VertexViewer

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph_ascii/VertexViewer)

VertexViewer class.

Class to define vertex box boundaries that will be accounted for during
graph building by grandalf.

## Signature

```python
VertexViewer(
    self,
    name: str,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `name` | `str` | Yes | name of the vertex. |

## Constructors

```python
__init__(
    self,
    name: str,
) -> None
```

| Name | Type |
|------|------|
| `name` | `str` |

## Properties

- `HEIGHT`
- `h`
- `w`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/graph_ascii.py#L27)
