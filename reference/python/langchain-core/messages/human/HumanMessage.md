---
title: "HumanMessage"
description: "Message from the user."
source: "https://reference.langchain.com/python/langchain-core/messages/human/HumanMessage"
category: "reference"
tags: [reference, langchain-core, messages, human, humanmessage]
---

# HumanMessage

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/human/HumanMessage)

Message from the user.

A `HumanMessage` is a message that is passed in from a user to the model.

## Signature

```python
HumanMessage(
    self,
    content: str | list[str | dict[Any, Any]] | None = None,
    content_blocks: list[types.ContentBlock] | None = None,
    **kwargs: Any = {},
)
```

## Description

**Example:**

```python
from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="You are a helpful assistant! Your name is Bob."),
    HumanMessage(content="What is your name?"),
]

# Instantiate a chat model and invoke it with the messages
model = ...
print(model.invoke(messages))
```

## Extends

- `BaseMessage`

## Constructors

```python
__init__(
    self,
    content: str | list[str | dict[Any, Any]] | None = None,
    content_blocks: list[types.ContentBlock] | None = None,
    **kwargs: Any = {},
) -> None
```

| Name | Type |
|------|------|
| `content` | `str \| list[str \| dict[Any, Any]] \| None` |
| `content_blocks` | `list[types.ContentBlock] \| None` |

## Properties

- `type`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/messages/human.py#L9)
