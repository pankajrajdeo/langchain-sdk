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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/04ac76c07ec173a44e3e57de54861d0b637e3299/libs/core/langchain_core/chat_sessions.py#L9)
