---
title: "from_messages"
description: "Create a chat prompt template from a variety of message formats."
source: "https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/from_messages"
category: "reference"
tags: [reference, langchain-core, prompts, chat, chatprompttemplate, from_messages]
---

# from_messages

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/from_messages)

Create a chat prompt template from a variety of message formats.

## Signature

```python
from_messages(
    cls,
    messages: Sequence[MessageLikeRepresentation],
    template_format: PromptTemplateFormat = 'f-string',
) -> ChatPromptTemplate
```

## Description

Args:
messages: Sequence of message representations.

    A message can be represented using the following formats:

    1. `BaseMessagePromptTemplate`
    2. `BaseMessage`
    3. 2-tuple of `(message type, template)`; e.g.,
        `('human', '{user_input}')`
    4. 2-tuple of `(message class, template)`
    5. A string which is shorthand for `('human', template)`; e.g.,
        `'{user_input}'`
template_format: Format of the template.

## Returns

`ChatPromptTemplate`

A chat prompt template.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/prompts/chat.py#L1123)
