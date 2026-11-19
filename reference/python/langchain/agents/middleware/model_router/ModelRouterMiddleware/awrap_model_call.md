---
title: "awrap_model_call"
description: "Route an asynchronous model call to the selected model."
source: "https://reference.langchain.com/python/langchain/agents/middleware/model_router/ModelRouterMiddleware/awrap_model_call"
category: "reference"
tags: [reference, langchain, agents, middleware, model_router, modelroutermiddleware, awrap_model_call]
---

# awrap_model_call

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/model_router/ModelRouterMiddleware/awrap_model_call)

Route an asynchronous model call to the selected model.

## Signature

```python
awrap_model_call(
    self,
    request: ModelRequest[ContextT],
    handler: Callable[[ModelRequest[ContextT]], Awaitable[ModelResponse[ResponseT]]],
) -> ModelResponse[ResponseT]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ced9bdb1a8899516b6c541fc0e19ab5f349aa0ea/libs/langchain_v1/langchain/agents/middleware/model_router.py#L187)
