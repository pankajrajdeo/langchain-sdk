---
title: "format_messages"
description: "Format kwargs into a list of messages."
source: "https://reference.langchain.com/python/langchain-core/prompts/few_shot/FewShotChatMessagePromptTemplate/format_messages"
category: "reference"
tags: [reference, langchain-core, prompts, few_shot, fewshotchatmessageprompttemplate, format_messages]
---

# format_messages

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/few_shot/FewShotChatMessagePromptTemplate/format_messages)

Format kwargs into a list of messages.

## Signature

```python
format_messages(
    self,
    **kwargs: Any = {},
) -> list[BaseMessage]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `**kwargs` | `Any` | No | Keyword arguments to use for filling in templates in messages. (default: `{}`) |

## Returns

`list[BaseMessage]`

A list of formatted messages with all template variables filled in.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/prompts/few_shot.py#L397)
