---
title: "awrap_model_call"
description: "(async) Update the system message to include instructions on using subagents."
source: "https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgentMiddleware/awrap_model_call"
category: "reference"
tags: [reference, deepagents, middleware, subagents, subagentmiddleware, awrap_model_call]
---

# awrap_model_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgentMiddleware/awrap_model_call)

(async) Update the system message to include instructions on using subagents.

## Signature

```python
awrap_model_call(
    self,
    request: ModelRequest[ContextT],
    handler: Callable[[ModelRequest[ContextT]], Awaitable[ModelResponse[ResponseT]]],
) -> ModelResponse[ResponseT]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9b754bc914cc75c3f6d8c6e99353e81041b73bce/libs/deepagents/deepagents/middleware/subagents.py#L1168)
