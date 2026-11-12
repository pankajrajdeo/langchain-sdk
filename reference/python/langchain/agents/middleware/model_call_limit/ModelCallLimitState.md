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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c2f4036e4c6ca45a8da8a42d8e07a25d2ea48b8f/libs/langchain_v1/langchain/agents/middleware/model_call_limit.py#L24)
