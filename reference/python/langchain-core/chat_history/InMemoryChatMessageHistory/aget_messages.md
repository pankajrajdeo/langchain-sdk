---
title: "aget_messages"
description: "Async version of getting messages."
source: "https://reference.langchain.com/python/langchain-core/chat_history/InMemoryChatMessageHistory/aget_messages"
category: "reference"
tags: [reference, langchain-core, chat_history, inmemorychatmessagehistory, aget_messages]
---

# aget_messages

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/chat_history/InMemoryChatMessageHistory/aget_messages)

Async version of getting messages.

Can over-ride this method to provide an efficient async implementation.

In general, fetching messages may involve IO to the underlying persistence
layer.

## Signature

```python
aget_messages(
    self,
) -> list[BaseMessage]
```

## Returns

`list[BaseMessage]`

List of messages.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/chat_history.py#L211)
