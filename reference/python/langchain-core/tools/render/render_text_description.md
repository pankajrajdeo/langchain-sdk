---
title: "render_text_description"
description: "Render the tool name and description in plain text."
source: "https://reference.langchain.com/python/langchain-core/tools/render/render_text_description"
category: "reference"
tags: [reference, langchain-core, tools, render, render_text_description]
---

# render_text_description

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/render/render_text_description)

Render the tool name and description in plain text.

## Signature

```python
render_text_description(
    tools: list[BaseTool],
) -> str
```

## Description

Output will be in the format of:

```txt
search: This tool is used for search
calculator: This tool is used for math
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `tools` | `list[BaseTool]` | Yes | The tools to render. |

## Returns

`str`

The rendered text.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/tools/render.py#L13)
