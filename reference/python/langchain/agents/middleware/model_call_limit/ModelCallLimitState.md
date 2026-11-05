---
title: "ModelCallLimitState"
description: "State schema for ModelCallLimitMiddleware."
source: "https://reference.langchain.com/python/langchain/agents/middleware/model_call_limit/ModelCallLimitState"
category: "reference"
tags: [reference, langchain, agents, middleware, model_call_limit, modelcalllimitstate]
---

# ModelCallLimitState

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/model_call_limit/ModelCallLimitState)

State schema for `ModelCallLimitMiddleware`.

Extends `AgentState` with model call tracking fields.

## Signature

```python
ModelCallLimitState()
```

## Extends

- `AgentState[ResponseT]`

## Properties

- `thread_model_call_count`
- `run_model_call_count`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d1d95b79213b0212613ae1aa4fad38bea6f1dccf/libs/langchain_v1/langchain/agents/middleware/model_call_limit.py#L24)
