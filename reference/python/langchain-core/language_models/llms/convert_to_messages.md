---
title: "convert_to_messages"
description: "Convert a sequence of messages to a list of messages."
source: "https://reference.langchain.com/python/langchain-core/language_models/llms/convert_to_messages"
category: "reference"
tags: [reference, langchain-core, language_models, llms, convert_to_messages]
---

# convert_to_messages

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/utils/convert_to_messages)

Convert a sequence of messages to a list of messages.

## Signature

```python
convert_to_messages(
    messages: Iterable[MessageLikeRepresentation] | PromptValue,
) -> list[BaseMessage]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `messages` | `Iterable[MessageLikeRepresentation] \| PromptValue` | Yes | Sequence of messages to convert. |

## Returns

`list[BaseMessage]`

list of messages (BaseMessages).

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/messages/utils.py#L799)
