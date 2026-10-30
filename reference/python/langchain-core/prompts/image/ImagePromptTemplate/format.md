---
title: "format"
description: "Format the prompt with the inputs."
source: "https://reference.langchain.com/python/langchain-core/prompts/image/ImagePromptTemplate/format"
category: "reference"
tags: [reference, langchain-core, prompts, image, imageprompttemplate, format]
---

# format

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/image/ImagePromptTemplate/format)

Format the prompt with the inputs.

## Signature

```python
format(
    self,
    kwargs: Any = {},
) -> ImageURL
```

## Description

**Example:**

```python
prompt.format(variable1="foo")
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `**kwargs` | `Any` | No | Any arguments to be passed to the prompt template. (default: `{}`) |

## Returns

`ImageURL`

A formatted string.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/prompts/image.py#L104)
