---
title: "mustache_schema"
description: "Get the variables from a mustache template."
source: "https://reference.langchain.com/python/langchain-core/prompts/string/mustache_schema"
category: "reference"
tags: [reference, langchain-core, prompts, string, mustache_schema]
---

# mustache_schema

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/string/mustache_schema)

Get the variables from a mustache template.

## Signature

```python
mustache_schema(
    template: str,
) -> type[BaseModel]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `template` | `str` | Yes | The template string. |

## Returns

`type[BaseModel]`

The variables from the template as a Pydantic model.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d4dafe5839c4a6b07d71cc78697df0de9e627e21/libs/core/langchain_core/prompts/string.py#L158)
