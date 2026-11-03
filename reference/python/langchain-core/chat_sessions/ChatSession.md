---
title: "ChatSession"
description: "Chat Session."
source: "https://reference.langchain.com/python/langchain-core/chat_sessions/ChatSession"
category: "reference"
tags: [reference, langchain-core, chat_sessions, chatsession]
---

# ChatSession

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/chat_sessions/ChatSession)

Chat Session.

Chat Session represents a single conversation, channel, or other group of messages.

## Signature

```python
ChatSession()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    messages: Sequence[BaseMessage],
    functions: Sequence[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `messages` | `Sequence[BaseMessage]` |
| `functions` | `Sequence[dict[str, Any]]` |

## Properties

- `messages`
- `functions`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/e936943647fe9bd9c4c24122ee3e1812ead82130/libs/core/langchain_core/chat_sessions.py#L9)
