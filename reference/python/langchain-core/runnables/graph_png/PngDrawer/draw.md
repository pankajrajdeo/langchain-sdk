---
title: "draw"
description: "Draw the given state graph into a PNG file."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph_png/PngDrawer/draw"
category: "reference"
tags: [reference, langchain-core, runnables, graph_png, pngdrawer, draw]
---

# draw

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph_png/PngDrawer/draw)

Draw the given state graph into a PNG file.

Requires `graphviz` and `pygraphviz` to be installed.

## Signature

```python
draw(
    self,
    graph: Graph,
    output_path: str | None = None,
) -> bytes | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `Graph` | Yes | The graph to draw |
| `output_path` | `str \| None` | No | The path to save the PNG. If `None`, PNG bytes are returned. (default: `None`) |

## Returns

`bytes | None`

The PNG bytes if `output_path` is None, else None.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/runnables/graph_png.py#L120)
