---
title: "format_messages"
description: "Format the chat template into a list of finalized messages."
source: "https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/format_messages"
category: "reference"
tags: [reference, langchain-core, prompts, chat, chatprompttemplate, format_messages]
---

# format_messages

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/format_messages)

Format the chat template into a list of finalized messages.

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
| `**kwargs` | `Any` | No | Keyword arguments to use for filling in template variables in all the template messages in this chat template. (default: `{}`) |

## Returns

`list[BaseMessage]`

List of formatted messages.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/prompts/chat.py#L1174)
