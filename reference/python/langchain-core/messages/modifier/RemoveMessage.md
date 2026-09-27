---
title: "RemoveMessage"
description: "Message responsible for deleting other messages."
source: "https://reference.langchain.com/python/langchain-core/messages/modifier/RemoveMessage"
category: "reference"
tags: [reference, langchain-core, messages, modifier, removemessage]
---

# RemoveMessage

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/modifier/RemoveMessage)

Message responsible for deleting other messages.

## Signature

```python
RemoveMessage(
    self,
    id: str,
    **kwargs: Any = {},
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | `str` | Yes | The ID of the message to remove. |
| `**kwargs` | `Any` | No | Additional fields to pass to the message. (default: `{}`) |

## Extends

- `BaseMessage`

## Constructors

```python
__init__(
    self,
    id: str,
    **kwargs: Any = {},
) -> None
```

| Name | Type |
|------|------|
| `id` | `str` |

## Properties

- `type`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/messages/modifier.py#L8)
