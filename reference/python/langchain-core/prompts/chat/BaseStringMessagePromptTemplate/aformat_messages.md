---
title: "aformat_messages"
description: "Async format messages from kwargs."
source: "https://reference.langchain.com/python/langchain-core/prompts/chat/BaseStringMessagePromptTemplate/aformat_messages"
category: "reference"
tags: [reference, langchain-core, prompts, chat, basestringmessageprompttemplate, aformat_messages]
---

# aformat_messages

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/chat/BaseStringMessagePromptTemplate/aformat_messages)

Async format messages from kwargs.

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
| `**kwargs` | `Any` | No | Keyword arguments to use for formatting. (default: `{}`) |

## Returns

`list[BaseMessage]`

List of `BaseMessage` objects.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/prompts/chat.py#L318)
