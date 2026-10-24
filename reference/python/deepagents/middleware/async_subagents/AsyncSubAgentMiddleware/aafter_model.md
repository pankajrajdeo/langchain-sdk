---
title: "aafter_model"
description: "(async) After a final answer, check tasks once more; on a status update, give the model another turn."
source: "https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgentMiddleware/aafter_model"
category: "reference"
tags: [reference, deepagents, middleware, async_subagents, asyncsubagentmiddleware, aafter_model]
---

# aafter_model

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgentMiddleware/aafter_model)

(async) After a final answer, check tasks once more; on a status update, give the model another turn.

Each extra turn needs a new status update, so the tasks themselves bound how many there are.

## Signature

```python
aafter_model(
    self,
    state: AsyncSubAgentState,
    runtime: Runtime[ContextT],
) -> dict[str, Any] | None
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/middleware/async_subagents.py#L1630)
