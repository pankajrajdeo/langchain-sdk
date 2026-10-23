---
title: "InMemoryChatMessageHistory"
description: "In memory implementation of chat message history."
source: "https://reference.langchain.com/python/langchain-core/chat_history/InMemoryChatMessageHistory"
category: "reference"
tags: [reference, langchain-core, chat_history, inmemorychatmessagehistory]
---

# InMemoryChatMessageHistory

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/chat_history/InMemoryChatMessageHistory)

In memory implementation of chat message history.

Stores messages in a memory list.

## Signature

```python
InMemoryChatMessageHistory(
    self,
    args: Any = (),
    kwargs: Any = {},
)
```

## Extends

- `BaseChatMessageHistory`
- `BaseModel`

## Properties

- `messages`

## Methods

- [`aget_messages()`](https://reference.langchain.com/python/langchain-core/chat_history/InMemoryChatMessageHistory/aget_messages)
- [`add_message()`](https://reference.langchain.com/python/langchain-core/chat_history/InMemoryChatMessageHistory/add_message)
- [`aadd_messages()`](https://reference.langchain.com/python/langchain-core/chat_history/InMemoryChatMessageHistory/aadd_messages)
- [`clear()`](https://reference.langchain.com/python/langchain-core/chat_history/InMemoryChatMessageHistory/clear)
- [`aclear()`](https://reference.langchain.com/python/langchain-core/chat_history/InMemoryChatMessageHistory/aclear)

## ⚠️ Deprecated

Deprecated since version 1.6.4. Will be removed in version 2.0.0. See the short-term memory documentation for recommended alternatives: https://docs.langchain.com/oss/python/langchain/short-term-memory

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/bdf0f53ed0aec3c9ae371a549e1a4d2ee4e9f021/libs/core/langchain_core/chat_history.py#L215)
