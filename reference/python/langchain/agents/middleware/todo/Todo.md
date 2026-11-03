---
title: "Todo"
description: "A single todo item with content and status."
source: "https://reference.langchain.com/python/langchain/agents/middleware/todo/Todo"
category: "reference"
tags: [reference, langchain, agents, middleware, todo]
---

# Todo

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/todo/Todo)

A single todo item with content and status.

## Signature

```python
Todo()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    content: str,
    status: Literal['pending', 'in_progress', 'completed'],
)
```

| Name | Type |
|------|------|
| `content` | `str` |
| `status` | `Literal['pending', 'in_progress', 'completed']` |

## Properties

- `content`
- `status`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/5dcec1858191a6b54cd843dd8e54d856e2e007cc/libs/langchain_v1/langchain/agents/middleware/todo.py#L25)
