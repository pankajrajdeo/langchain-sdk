---
title: "format"
description: "Format the prompt with inputs generating a string."
source: "https://reference.langchain.com/python/langchain-core/prompts/few_shot/FewShotPromptTemplate/format"
category: "reference"
tags: [reference, langchain-core, prompts, few_shot, fewshotprompttemplate, format]
---

# format

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/few_shot/FewShotPromptTemplate/format)

Format the prompt with inputs generating a string.

Use this method to generate a string representation of a prompt.

## Signature

```python
format(
    self,
    **kwargs: Any = {},
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `**kwargs` | `Any` | No | Keyword arguments to use for formatting. (default: `{}`) |

## Returns

`str`

A string representation of the prompt.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/prompts/few_shot.py#L180)
