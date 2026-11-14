---
title: "before_model"
description: "Pass through: checking tasks needs the async path, which the Agent Server uses."
source: "https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgentMiddleware/before_model"
category: "reference"
tags: [reference, deepagents, middleware, async_subagents, asyncsubagentmiddleware, before_model]
---

# before_model

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgentMiddleware/before_model)

Pass through: checking tasks needs the async path, which the Agent Server uses.

## Signature

```python
before_model(
    self,
    state: AsyncSubAgentState,
    runtime: Runtime[ContextT],
) -> dict[str, Any] | None
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/c858b3641b13fb3f40fe3a12515517b81fb8a744/libs/deepagents/deepagents/middleware/async_subagents.py#L1653)
