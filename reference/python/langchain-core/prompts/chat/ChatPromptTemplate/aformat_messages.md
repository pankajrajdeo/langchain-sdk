---
title: "aformat_messages"
description: "Async format the chat template into a list of finalized messages."
source: "https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/aformat_messages"
category: "reference"
tags: [reference, langchain-core, prompts, chat, chatprompttemplate, aformat_messages]
---

# aformat_messages

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/aformat_messages)

Async format the chat template into a list of finalized messages.

## Signature

```python
aformat_messages(
    self,
    kwargs: Any = {},
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/6419339aa163a49f32d9b80ff20d6adc3b446d49/libs/core/langchain_core/prompts/chat.py#L1202)
