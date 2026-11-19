---
title: "abefore_agent"
description: "Classify the latest task asynchronously and store the routing answer."
source: "https://reference.langchain.com/python/langchain/agents/middleware/model_router/ModelRouterMiddleware/abefore_agent"
category: "reference"
tags: [reference, langchain, agents, middleware, model_router, modelroutermiddleware, abefore_agent]
---

# abefore_agent

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/model_router/ModelRouterMiddleware/abefore_agent)

Classify the latest task asynchronously and store the routing answer.

## Signature

```python
abefore_agent(
    self,
    state: _ModelRouterState,
    runtime: Runtime[ContextT],
) -> dict[str, ChoiceAnswer]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ced9bdb1a8899516b6c541fc0e19ab5f349aa0ea/libs/langchain_v1/langchain/agents/middleware/model_router.py#L164)
