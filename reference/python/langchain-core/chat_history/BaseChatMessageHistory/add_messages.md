---
title: "add_messages"
description: "Add a list of messages."
source: "https://reference.langchain.com/python/langchain-core/chat_history/BaseChatMessageHistory/add_messages"
category: "reference"
tags: [reference, langchain-core, chat_history, basechatmessagehistory, add_messages]
---

# add_messages

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/chat_history/BaseChatMessageHistory/add_messages)

Add a list of messages.

Implementations should over-ride this method to handle bulk addition of messages
in an efficient manner to avoid unnecessary round-trips to the underlying store.

## Signature

```python
add_messages(
    self,
    messages: Sequence[BaseMessage],
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `messages` | `Sequence[BaseMessage]` | Yes | A sequence of `BaseMessage` objects to store. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/chat_history.py#L169)
