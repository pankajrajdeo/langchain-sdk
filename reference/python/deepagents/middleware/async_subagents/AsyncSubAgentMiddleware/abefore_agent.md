---
title: "abefore_agent"
description: "(async) Record the notification that started this run, then add status updates from this agent's tasks."
source: "https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgentMiddleware/abefore_agent"
category: "reference"
tags: [reference, deepagents, middleware, async_subagents, asyncsubagentmiddleware, abefore_agent]
---

# abefore_agent

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgentMiddleware/abefore_agent)

(async) Record the notification that started this run, then add status updates from this agent's tasks.

## Signature

```python
abefore_agent(
    self,
    state: AsyncSubAgentState,
    runtime: Runtime[ContextT],
) -> dict[str, Any] | None
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/18930b5463c8a0a432353db5299af280f879973f/libs/deepagents/deepagents/middleware/async_subagents.py#L1640)
