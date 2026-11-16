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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ea17e48f0a4336c920394fd029de99f1568b4c38/libs/core/langchain_core/messages/chat.py#L15)
