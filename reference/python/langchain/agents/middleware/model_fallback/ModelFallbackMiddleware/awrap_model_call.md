---
title: "awrap_model_call"
description: "Try fallback models in sequence on errors (async version)."
source: "https://reference.langchain.com/python/langchain/agents/middleware/model_fallback/ModelFallbackMiddleware/awrap_model_call"
category: "reference"
tags: [reference, langchain, agents, middleware, model_fallback, modelfallbackmiddleware, awrap_model_call]
---

# awrap_model_call

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/model_fallback/ModelFallbackMiddleware/awrap_model_call)

Try fallback models in sequence on errors (async version).

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
| `request` | `ModelRequest[ContextT]` | Yes | Initial model request. |
| `handler` | `Callable[[ModelRequest[ContextT]], Awaitable[ModelResponse[ResponseT]]]` | Yes | Async callback to execute the model. |

## Returns

`ModelResponse[ResponseT] | AIMessage`

AIMessage from successful model call.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/5dcec1858191a6b54cd843dd8e54d856e2e007cc/libs/langchain_v1/langchain/agents/middleware/model_fallback.py#L432)
