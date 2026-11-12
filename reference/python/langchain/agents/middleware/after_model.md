---
title: "after_model"
description: "Increment model call counts after a model call."
source: "https://reference.langchain.com/python/langchain/agents/middleware/after_model"
category: "reference"
tags: [reference, langchain, agents, middleware, after_model]
---

# after_model

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/model_call_limit/ModelCallLimitMiddleware/after_model)

Increment model call counts after a model call.

## Signature

```python
after_model(
    self,
    state: ModelCallLimitState[ResponseT],
    runtime: Runtime[ContextT],
) -> dict[str, Any] | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `state` | `ModelCallLimitState[ResponseT]` | Yes | The current agent state. |
| `runtime` | `Runtime[ContextT]` | Yes | The langgraph runtime. |

## Returns

`dict[str, Any] | None`

State updates with incremented call counts.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c2f4036e4c6ca45a8da8a42d8e07a25d2ea48b8f/libs/langchain_v1/langchain/agents/middleware/model_call_limit.py#L235)
