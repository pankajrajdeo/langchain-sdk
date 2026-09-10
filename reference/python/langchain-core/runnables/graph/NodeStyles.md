---
title: "NodeStyles"
description: "Schema for Hexadecimal color codes for different node types."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph/NodeStyles"
category: "reference"
tags: [reference, langchain-core, runnables, graph, nodestyles]
---

# NodeStyles

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph/NodeStyles)

Schema for Hexadecimal color codes for different node types.

## Signature

```python
NodeStyles(
    self,
    default: str = 'fill:#f2f0ff,line-height:1.2',
    first: str = 'fill-opacity:0',
    last: str = 'fill:#bfb6fc',
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `default` | `str` | No | The default color code. (default: `'fill:#f2f0ff,line-height:1.2'`) |
| `first` | `str` | No | The color code for the first node. (default: `'fill-opacity:0'`) |
| `last` | `str` | No | The color code for the last node. (default: `'fill:#bfb6fc'`) |

## Constructors

```python
__init__(
    self,
    default: str = 'fill:#f2f0ff,line-height:1.2',
    first: str = 'fill-opacity:0',
    last: str = 'fill:#bfb6fc',
) -> None
```

| Name | Type |
|------|------|
| `default` | `str` |
| `first` | `str` |
| `last` | `str` |

## Properties

- `default`
- `first`
- `last`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/graph.py#L156)
