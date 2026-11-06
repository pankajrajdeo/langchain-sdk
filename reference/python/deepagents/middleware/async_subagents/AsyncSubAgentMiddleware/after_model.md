---
title: "after_model"
description: "Pass through: checking tasks needs the async path, which the Agent Server uses."
source: "https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgentMiddleware/after_model"
category: "reference"
tags: [reference, deepagents, middleware, async_subagents, asyncsubagentmiddleware, after_model]
---

# after_model

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgentMiddleware/after_model)

Pass through: checking tasks needs the async path, which the Agent Server uses.

## Signature

```python
after_model(
    self,
    state: AsyncSubAgentState,
    runtime: Runtime[ContextT],
) -> dict[str, Any] | None
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9ea3f1912abd8b7eecb504d78ef99fcf279bf561/libs/deepagents/deepagents/middleware/async_subagents.py#L1661)
