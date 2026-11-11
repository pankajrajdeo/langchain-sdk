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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c0344e0cee824c1c6489ba972cea171ff193d234/libs/langchain_v1/langchain/agents/middleware/todo.py#L25)
