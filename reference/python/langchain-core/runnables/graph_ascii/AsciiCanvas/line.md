---
title: "line"
description: "Create a line on ASCII canvas."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph_ascii/AsciiCanvas/line"
category: "reference"
tags: [reference, langchain-core, runnables, graph_ascii, asciicanvas, line]
---

# line

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph_ascii/AsciiCanvas/line)

Create a line on ASCII canvas.

## Signature

```python
line(
    self,
    x0: int,
    y0: int,
    x1: int,
    y1: int,
    char: str,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `x0` | `int` | Yes | x coordinate where the line should start. |
| `y0` | `int` | Yes | y coordinate where the line should start. |
| `x1` | `int` | Yes | x coordinate where the line should end. |
| `y1` | `int` | Yes | y coordinate where the line should end. |
| `char` | `str` | Yes | character to draw the line with. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/graph_ascii.py#L117)
