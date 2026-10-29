---
title: "draw_png"
description: "Draw the graph as a PNG image."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/draw_png"
category: "reference"
tags: [reference, langchain-core, runnables, graph, draw_png]
---

# draw_png

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/draw_png)

Draw the graph as a PNG image.

## Signature

```python
draw_png(
    self,
    output_file_path: str | None = None,
    fontname: str | None = None,
    labels: LabelsDict | None = None,
) -> bytes | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `output_file_path` | `str \| None` | No | The path to save the image to. If `None`, the image is not saved. (default: `None`) |
| `fontname` | `str \| None` | No | The name of the font to use. (default: `None`) |
| `labels` | `LabelsDict \| None` | No | Optional labels for nodes and edges in the graph. Defaults to `None`. (default: `None`) |

## Returns

`bytes | None`

The PNG image as bytes if output_file_path is None, None otherwise.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/6419339aa163a49f32d9b80ff20d6adc3b446d49/libs/core/langchain_core/runnables/graph.py#L546)
