---
title: "awrap_model_call"
description: "Intercept and control async model execution with retry logic."
source: "https://reference.langchain.com/python/langchain/agents/middleware/model_retry/ModelRetryMiddleware/awrap_model_call"
category: "reference"
tags: [reference, langchain, agents, middleware, model_retry, modelretrymiddleware, awrap_model_call]
---

# awrap_model_call

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/model_retry/ModelRetryMiddleware/awrap_model_call)

Intercept and control async model execution with retry logic.

## Signature

```python
awrap_model_call(
    self,
    request: ModelRequest[ContextT],
    handler: Callable[[ModelRequest[ContextT]], Awaitable[ModelResponse[ResponseT]]],
) -> ModelResponse[ResponseT] | AIMessage
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | `ModelRequest[ContextT]` | Yes | Model request with model, messages, state, and runtime. |
| `handler` | `Callable[[ModelRequest[ContextT]], Awaitable[ModelResponse[ResponseT]]]` | Yes | Async callable to execute the model and returns `ModelResponse`. |

## Returns

`ModelResponse[ResponseT] | AIMessage`

`ModelResponse` or `AIMessage` (the final result).

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/be854a130153e51346d83d3b06f959b80f6cbca6/libs/langchain_v1/langchain/agents/middleware/model_retry.py#L275)
