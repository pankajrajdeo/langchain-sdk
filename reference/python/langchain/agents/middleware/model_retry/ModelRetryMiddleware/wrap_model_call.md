---
title: "wrap_model_call"
description: "Intercept model execution and retry on failure."
source: "https://reference.langchain.com/python/langchain/agents/middleware/model_retry/ModelRetryMiddleware/wrap_model_call"
category: "reference"
tags: [reference, langchain, agents, middleware, model_retry, modelretrymiddleware, wrap_model_call]
---

# wrap_model_call

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/model_retry/ModelRetryMiddleware/wrap_model_call)

Intercept model execution and retry on failure.

## Signature

```python
wrap_model_call(
    self,
    request: ModelRequest[ContextT],
    handler: Callable[[ModelRequest[ContextT]], ModelResponse[ResponseT]],
) -> ModelResponse[ResponseT] | AIMessage
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | `ModelRequest[ContextT]` | Yes | Model request with model, messages, state, and runtime. |
| `handler` | `Callable[[ModelRequest[ContextT]], ModelResponse[ResponseT]]` | Yes | Callable to execute the model (can be called multiple times). |

## Returns

`ModelResponse[ResponseT] | AIMessage`

`ModelResponse` or `AIMessage` (the final result).

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/middleware/model_retry.py#L221)
