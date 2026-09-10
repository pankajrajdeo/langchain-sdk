---
title: "before_model"
description: "Check user messages and tool results for PII before model invocation."
source: "https://reference.langchain.com/python/langchain/agents/middleware/pii/PIIMiddleware/before_model"
category: "reference"
tags: [reference, langchain, agents, middleware, pii, piimiddleware, before_model]
---

# before_model

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/pii/PIIMiddleware/before_model)

Check user messages and tool results for PII before model invocation.

## Signature

```python
before_model(
    self,
    state: AgentState[Any],
    runtime: Runtime[ContextT],
) -> dict[str, Any] | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `state` | `AgentState[Any]` | Yes | The current agent state. |
| `runtime` | `Runtime[ContextT]` | Yes | The langgraph runtime. |

## Returns

`dict[str, Any] | None`

Updated state with PII handled according to strategy, or `None` if no PII
detected.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/middleware/pii.py#L697)
