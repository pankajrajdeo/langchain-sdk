---
title: "add_ai_message"
description: "Convenience method for adding an AIMessage string to the store."
source: "https://reference.langchain.com/python/langchain-core/chat_history/BaseChatMessageHistory/add_ai_message"
category: "reference"
tags: [reference, langchain-core, chat_history, basechatmessagehistory, add_ai_message]
---

# add_ai_message

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/chat_history/BaseChatMessageHistory/add_ai_message)

Convenience method for adding an `AIMessage` string to the store.

!!! note

    This is a convenience method. Code should favor the bulk `add_messages`
    interface instead to save on round-trips to the persistence layer.

This method may be deprecated in a future release.

## Signature

```python
add_ai_message(
    self,
    message: AIMessage | str,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `message` | `AIMessage \| str` | Yes | The `AIMessage` to add. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/chat_history.py#L143)
