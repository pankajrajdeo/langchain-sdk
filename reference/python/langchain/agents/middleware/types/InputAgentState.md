---
title: "InputAgentState"
description: "Input state schema for the agent."
source: "https://reference.langchain.com/python/langchain/agents/middleware/types/InputAgentState"
category: "reference"
tags: [reference, langchain, agents, middleware, types, inputagentstate]
---

# InputAgentState

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/types/InputAgentState)

Input state schema for the agent.

## Signature

```python
InputAgentState()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    messages: Required[Annotated[list[AnyMessage | dict[str, Any]], add_messages]],
)
```

| Name | Type |
|------|------|
| `messages` | `Required[Annotated[list[AnyMessage \| dict[str, Any]], add_messages]]` |

## Properties

- `messages`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ced9bdb1a8899516b6c541fc0e19ab5f349aa0ea/libs/langchain_v1/langchain/agents/middleware/types.py#L359)
