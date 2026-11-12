---
title: "before_agent"
description: "Classify the latest task and store the complete routing answer."
source: "https://reference.langchain.com/python/langchain/agents/middleware/before_agent"
category: "reference"
tags: [reference, langchain, agents, middleware, before_agent]
---

# before_agent

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/model_router/ModelRouterMiddleware/before_agent)

Classify the latest task and store the complete routing answer.

## Signature

```python
before_agent(
    self,
    state: _ModelRouterState,
    runtime: Runtime[ContextT],
) -> dict[str, ChoiceAnswer]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c2f4036e4c6ca45a8da8a42d8e07a25d2ea48b8f/libs/langchain_v1/langchain/agents/middleware/model_router.py#L151)
