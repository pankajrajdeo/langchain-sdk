---
title: "before_agent"
description: "Logic to run before the agent execution starts."
source: "https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/before_agent"
category: "reference"
tags: [reference, langchain, agents, middleware, types, agentmiddleware, before_agent]
---

# before_agent

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/before_agent)

Logic to run before the agent execution starts.

## Signature

```python
before_agent(
    self,
    state: StateT,
    runtime: Runtime[ContextT],
) -> dict[str, Any] | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `state` | `StateT` | Yes | The current agent state. |
| `runtime` | `Runtime[ContextT]` | Yes | The runtime context. |

## Returns

`dict[str, Any] | None`

Agent state updates to apply before agent execution.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/be854a130153e51346d83d3b06f959b80f6cbca6/libs/langchain_v1/langchain/agents/middleware/types.py#L431)
