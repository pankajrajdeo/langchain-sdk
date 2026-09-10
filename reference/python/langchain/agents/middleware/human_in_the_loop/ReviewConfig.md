---
title: "ReviewConfig"
description: "Policy for reviewing a HITL request."
source: "https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/ReviewConfig"
category: "reference"
tags: [reference, langchain, agents, middleware, human_in_the_loop, reviewconfig]
---

# ReviewConfig

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/ReviewConfig)

Policy for reviewing a HITL request.

## Signature

```python
ReviewConfig()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    action_name: str,
    allowed_decisions: list[DecisionType],
    args_schema: NotRequired[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `action_name` | `str` |
| `allowed_decisions` | `list[DecisionType]` |
| `args_schema` | `NotRequired[dict[str, Any]]` |

## Properties

- `action_name`
- `allowed_decisions`
- `args_schema`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L54)
