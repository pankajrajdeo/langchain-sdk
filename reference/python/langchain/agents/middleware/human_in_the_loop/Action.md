---
title: "Action"
description: "Represents an action with a name and args."
source: "https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/Action"
category: "reference"
tags: [reference, langchain, agents, middleware, human_in_the_loop, action]
---

# Action

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/Action)

Represents an action with a name and args.

## Signature

```python
Action()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    name: str,
    args: dict[str, Any],
)
```

| Name | Type |
|------|------|
| `name` | `str` |
| `args` | `dict[str, Any]` |

## Properties

- `name`
- `args`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c0344e0cee824c1c6489ba972cea171ff193d234/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L63)
