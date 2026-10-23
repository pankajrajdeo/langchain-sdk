---
title: "format"
description: "Format the chat template into a string."
source: "https://reference.langchain.com/python/langchain-core/prompts/chat/BaseChatPromptTemplate/format"
category: "reference"
tags: [reference, langchain-core, prompts, chat, basechatprompttemplate, format]
---

# format

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/chat/BaseChatPromptTemplate/format)

Format the chat template into a string.

## Signature

```python
format(
    self,
    kwargs: Any = {},
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `**kwargs` | `Any` | No | Keyword arguments to use for filling in template variables in all the template messages in this chat template. (default: `{}`) |

## Returns

`str`

Formatted string.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/prompts/chat.py#L703)
