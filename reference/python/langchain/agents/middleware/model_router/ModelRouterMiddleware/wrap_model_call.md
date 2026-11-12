---
title: "wrap_model_call"
description: "Route a synchronous model call to the selected model."
source: "https://reference.langchain.com/python/langchain/agents/middleware/model_router/ModelRouterMiddleware/wrap_model_call"
category: "reference"
tags: [reference, langchain, agents, middleware, model_router, modelroutermiddleware, wrap_model_call]
---

# wrap_model_call

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/model_router/ModelRouterMiddleware/wrap_model_call)

Route a synchronous model call to the selected model.

## Signature

```python
wrap_model_call(
    self,
    request: ModelRequest[ContextT],
    handler: Callable[[ModelRequest[ContextT]], ModelResponse[ResponseT]],
) -> ModelResponse[ResponseT]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c2f4036e4c6ca45a8da8a42d8e07a25d2ea48b8f/libs/langchain_v1/langchain/agents/middleware/model_router.py#L177)
