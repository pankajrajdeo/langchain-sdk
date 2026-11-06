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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9ea3f1912abd8b7eecb504d78ef99fcf279bf561/libs/deepagents/deepagents/middleware/async_subagents.py#L1640)
