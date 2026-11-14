---
title: "before_agent"
description: "Record the task notification that started this run, if one did."
source: "https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgentMiddleware/before_agent"
category: "reference"
tags: [reference, deepagents, middleware, async_subagents, asyncsubagentmiddleware, before_agent]
---

# before_agent

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgentMiddleware/before_agent)

Record the task notification that started this run, if one did.

## Signature

```python
before_agent(
    self,
    state: AsyncSubAgentState,
    runtime: Runtime[ContextT],
) -> dict[str, Any] | None
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/c858b3641b13fb3f40fe3a12515517b81fb8a744/libs/deepagents/deepagents/middleware/async_subagents.py#L1636)
