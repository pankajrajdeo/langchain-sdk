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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c2f4036e4c6ca45a8da8a42d8e07a25d2ea48b8f/libs/langchain_v1/langchain/agents/middleware/model_router.py#L187)
