---
title: "ChatMessage"
description: "Message that can be assigned an arbitrary speaker (i.e. role)."
source: "https://reference.langchain.com/python/langchain-core/messages/chat/ChatMessage"
category: "reference"
tags: [reference, langchain-core, messages, chat, chatmessage]
---

# ChatMessage

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/chat/ChatMessage)

Message that can be assigned an arbitrary speaker (i.e. role).

## Signature

```python
ChatMessage(
    self,
    content: str | list[str | dict[Any, Any]] | None = None,
    content_blocks: list[types.ContentBlock] | None = None,
    kwargs: Any = {},
)
```

## Extends

- `BaseMessage`

## Properties

- `role`
- `type`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d4dafe5839c4a6b07d71cc78697df0de9e627e21/libs/core/langchain_core/messages/chat.py#L15)
