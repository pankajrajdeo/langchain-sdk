---
title: "aformat_messages"
description: "Async format messages from kwargs."
source: "https://reference.langchain.com/python/langchain-core/prompts/message/BaseMessagePromptTemplate/aformat_messages"
category: "reference"
tags: [reference, langchain-core, prompts, message, basemessageprompttemplate, aformat_messages]
---

# aformat_messages

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/message/BaseMessagePromptTemplate/aformat_messages)

Async format messages from kwargs.

## Signature

```python
aformat_messages(
    self,
    **kwargs: Any = {},
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/prompts/message.py#L46)
