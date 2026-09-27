---
title: "wrap_model_call"
description: "Update the system message to include instructions on using subagents."
source: "https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgentMiddleware/wrap_model_call"
category: "reference"
tags: [reference, deepagents, middleware, subagents, subagentmiddleware, wrap_model_call]
---

# wrap_model_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgentMiddleware/wrap_model_call)

Update the system message to include instructions on using subagents.

## Signature

```python
wrap_model_call(
    self,
    request: ModelRequest[ContextT],
    handler: Callable[[ModelRequest[ContextT]], ModelResponse[ResponseT]],
) -> ModelResponse[ResponseT]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/bb49cf50d3450a3bbebe8d25240cb7ef6379bd0d/libs/deepagents/deepagents/middleware/subagents.py#L1008)
