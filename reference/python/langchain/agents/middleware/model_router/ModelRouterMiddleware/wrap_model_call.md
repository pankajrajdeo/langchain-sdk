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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ced9bdb1a8899516b6c541fc0e19ab5f349aa0ea/libs/langchain_v1/langchain/agents/middleware/model_router.py#L177)
