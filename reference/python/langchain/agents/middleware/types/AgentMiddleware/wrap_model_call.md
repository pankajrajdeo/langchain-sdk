---
title: "wrap_model_call"
description: "Intercept and control model execution via handler callback."
source: "https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/wrap_model_call"
category: "reference"
tags: [reference, langchain, agents, middleware, types, agentmiddleware, wrap_model_call]
---

# wrap_model_call

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/wrap_model_call)

Intercept and control model execution via handler callback.

Async version is `awrap_model_call`

The handler callback executes the model request and returns a `ModelResponse`.
Middleware can call the handler multiple times for retry logic, skip calling
it to short-circuit, or modify the request/response. Multiple middleware
compose with first in list as outermost layer.

## Signature

```python
wrap_model_call(
    self,
    request: ModelRequest[ContextT],
    handler: Callable[[ModelRequest[ContextT]], ModelResponse[ResponseT]],
) -> ModelResponse[ResponseT] | AIMessage | ExtendedModelResponse[ResponseT]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | `ModelRequest[ContextT]` | Yes | Model request to execute (includes state and runtime). |
| `handler` | `Callable[[ModelRequest[ContextT]], ModelResponse[ResponseT]]` | Yes | Callback that executes the model request and returns `ModelResponse`.  Call this to execute the model.  Can be called multiple times for retry logic.  Can skip calling it to short-circuit. |

## Returns

`ModelResponse[ResponseT] | AIMessage | ExtendedModelResponse[ResponseT]`

The model call result.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/be854a130153e51346d83d3b06f959b80f6cbca6/libs/langchain_v1/langchain/agents/middleware/types.py#L503)
