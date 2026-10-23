---
title: "point"
description: "Create a point on ASCII canvas."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph_ascii/AsciiCanvas/point"
category: "reference"
tags: [reference, langchain-core, runnables, graph_ascii, asciicanvas, point]
---

# point

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph_ascii/AsciiCanvas/point)

Create a point on ASCII canvas.

## Signature

```python
point(
    self,
    x: int,
    y: int,
    char: str,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `x` | `int` | Yes | x coordinate. Should be `>= 0` and `<` number of columns in the canvas. |
| `y` | `int` | Yes | y coordinate. Should be `>= 0` an `<` number of lines in the canvas. |
| `char` | `str` | Yes | character to place in the specified point on the canvas. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/runnables/graph_ascii.py#L90)
