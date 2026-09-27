---
title: "aformat_prompt"
description: "Async format the prompt with the inputs."
source: "https://reference.langchain.com/python/langchain-core/prompts/string/StringPromptTemplate/aformat_prompt"
category: "reference"
tags: [reference, langchain-core, prompts, string, stringprompttemplate, aformat_prompt]
---

# aformat_prompt

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/string/StringPromptTemplate/aformat_prompt)

Async format the prompt with the inputs.

## Signature

```python
aformat_prompt(
    self,
    **kwargs: Any = {},
) -> PromptValue
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `**kwargs` | `Any` | No | Any arguments to be passed to the prompt template. (default: `{}`) |

## Returns

`PromptValue`

A formatted string.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/prompts/string.py#L351)
