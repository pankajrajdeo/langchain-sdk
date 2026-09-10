---
title: "get_color_mapping"
description: "Get mapping for items to a support color."
source: "https://reference.langchain.com/python/langchain-core/utils/input/get_color_mapping"
category: "reference"
tags: [reference, langchain-core, utils, input, get_color_mapping]
---

# get_color_mapping

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/input/get_color_mapping)

Get mapping for items to a support color.

## Signature

```python
get_color_mapping(
    items: list[str],
    excluded_colors: list[str] | None = None,
) -> dict[str, str]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `items` | `list[str]` | Yes | The items to map to colors. |
| `excluded_colors` | `list[str] \| None` | No | The colors to exclude. (default: `None`) |

## Returns

`dict[str, str]`

The mapping of items to colors.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/utils/input.py#L14)
