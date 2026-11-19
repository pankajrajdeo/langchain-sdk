---
title: "OutputAgentState"
description: "Output state schema for the agent."
source: "https://reference.langchain.com/python/langchain/agents/middleware/types/OutputAgentState"
category: "reference"
tags: [reference, langchain, agents, middleware, types, outputagentstate]
---

# OutputAgentState

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/types/OutputAgentState)

Output state schema for the agent.

## Signature

```python
OutputAgentState()
```

## Extends

- `TypedDict`
- `Generic[ResponseT]`

## Constructors

```python
__init__(
    messages: Required[Annotated[list[AnyMessage], add_messages]],
    structured_response: NotRequired[ResponseT],
)
```

| Name | Type |
|------|------|
| `messages` | `Required[Annotated[list[AnyMessage], add_messages]]` |
| `structured_response` | `NotRequired[ResponseT]` |

## Properties

- `messages`
- `structured_response`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ced9bdb1a8899516b6c541fc0e19ab5f349aa0ea/libs/langchain_v1/langchain/agents/middleware/types.py#L365)
