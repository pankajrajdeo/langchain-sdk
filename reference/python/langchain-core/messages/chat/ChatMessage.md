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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/b4aa7e7d00c452251720ce30b8bc2c41ca44e1f5/libs/core/langchain_core/messages/chat.py#L15)
