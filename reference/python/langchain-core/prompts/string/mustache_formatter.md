---
title: "mustache_formatter"
description: "Format a template using mustache."
source: "https://reference.langchain.com/python/langchain-core/prompts/string/mustache_formatter"
category: "reference"
tags: [reference, langchain-core, prompts, string, mustache_formatter]
---

# mustache_formatter

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/string/mustache_formatter)

Format a template using mustache.

## Signature

```python
mustache_formatter(
    template: str,
    /,
    **kwargs: Any = {},
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `template` | `str` | Yes | The template string. |
| `**kwargs` | `Any` | No | The variables to format the template with. (default: `{}`) |

## Returns

`str`

The formatted string.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/prompts/string.py#L112)
