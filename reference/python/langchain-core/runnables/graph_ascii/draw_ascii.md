---
title: "draw_ascii"
description: "Build a DAG and draw it in ASCII."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph_ascii/draw_ascii"
category: "reference"
tags: [reference, langchain-core, runnables, graph_ascii, draw_ascii]
---

# draw_ascii

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph_ascii/draw_ascii)

Build a DAG and draw it in ASCII.

## Signature

```python
draw_ascii(
    vertices: Mapping[str, str],
    edges: Sequence[LangEdge],
) -> str
```

## Description

**Example:**

```python
from langchain_core.runnables.graph_ascii import draw_ascii

vertices = {1: "1", 2: "2", 3: "3", 4: "4"}
edges = [
    (source, target, None, None)
    for source, target in [(1, 2), (2, 3), (2, 4), (1, 4)]
]

print(draw_ascii(vertices, edges))
```

```txt

         +---+
         | 1 |
         +---+
         *    *
        *     *
       *       *
    +---+       *
    | 2 |       *
    +---+**     *
      *    **   *
      *      ** *
      *        **
    +---+     +---+
    | 3 |     | 4 |
    +---+     +---+
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `vertices` | `Mapping[str, str]` | Yes | list of graph vertices. |
| `edges` | `Sequence[LangEdge]` | Yes | list of graph edges. |

## Returns

`str`

ASCII representation

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/graph_ascii.py#L247)
