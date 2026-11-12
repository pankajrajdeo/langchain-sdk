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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c2f4036e4c6ca45a8da8a42d8e07a25d2ea48b8f/libs/langchain_v1/langchain/agents/middleware/types.py#L365)
