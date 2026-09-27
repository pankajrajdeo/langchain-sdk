---
title: "indent_lines_after_first"
description: "Indent all lines of text after the first line."
source: "https://reference.langchain.com/python/langchain-core/runnables/utils/indent_lines_after_first"
category: "reference"
tags: [reference, langchain-core, runnables, utils, indent_lines_after_first]
---

# indent_lines_after_first

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/indent_lines_after_first)

Indent all lines of text after the first line.

## Signature

```python
indent_lines_after_first(
    text: str,
    prefix: str,
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | `str` | Yes | The text to indent. |
| `prefix` | `str` | Yes | Used to determine the number of spaces to indent. |

## Returns

`str`

The indented text.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/runnables/utils.py#L453)
