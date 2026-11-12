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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/messages/chat.py#L15)
