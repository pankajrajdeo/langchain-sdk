---
title: "text"
description: "Print a text on ASCII canvas."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph_ascii/AsciiCanvas/text"
category: "reference"
tags: [reference, langchain-core, runnables, graph_ascii, asciicanvas, text]
---

# text

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph_ascii/AsciiCanvas/text)

Print a text on ASCII canvas.

## Signature

```python
text(
    self,
    x: int,
    y: int,
    text: str,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `x` | `int` | Yes | x coordinate where the text should start. |
| `y` | `int` | Yes | y coordinate where the text should start. |
| `text` | `str` | Yes | string that should be printed. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/graph_ascii.py#L149)
