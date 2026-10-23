---
title: "aformat"
description: "Async format the prompt with inputs generating a string."
source: "https://reference.langchain.com/python/langchain-core/prompts/few_shot/FewShotChatMessagePromptTemplate/aformat"
category: "reference"
tags: [reference, langchain-core, prompts, few_shot, fewshotchatmessageprompttemplate, aformat]
---

# aformat

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/few_shot/FewShotChatMessagePromptTemplate/aformat)

Async format the prompt with inputs generating a string.

Use this method to generate a string representation of a prompt consisting of
chat messages.

Useful for feeding into a string-based completion language model or debugging.

## Signature

```python
aformat(
    self,
    kwargs: Any = {},
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `**kwargs` | `Any` | No | Keyword arguments to use for formatting. (default: `{}`) |

## Returns

`str`

A string representation of the prompt

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/prompts/few_shot.py#L456)
