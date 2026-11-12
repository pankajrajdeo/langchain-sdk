---
title: "RejectDecision"
description: "Response when a human rejects the action."
source: "https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/RejectDecision"
category: "reference"
tags: [reference, langchain, agents, middleware, human_in_the_loop, rejectdecision]
---

# RejectDecision

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/RejectDecision)

Response when a human rejects the action.

## Signature

```python
RejectDecision()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['reject'],
    message: NotRequired[str],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['reject']` |
| `message` | `NotRequired[str]` |

## Properties

- `type`
- `message`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c2f4036e4c6ca45a8da8a42d8e07a25d2ea48b8f/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L137)
