---
title: "wrap_model_call"
description: "Wrap model call to inject memory into system prompt."
source: "https://reference.langchain.com/python/deepagents/middleware/memory/MemoryMiddleware/wrap_model_call"
category: "reference"
tags: [reference, deepagents, middleware, memory, memorymiddleware, wrap_model_call]
---

# wrap_model_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/memory/MemoryMiddleware/wrap_model_call)

Wrap model call to inject memory into system prompt.

## Signature

```python
wrap_model_call(
    self,
    request: ModelRequest[ContextT],
    handler: Callable[[ModelRequest[ContextT]], ModelResponse[ResponseT]],
) -> ModelResponse[ResponseT]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | `ModelRequest[ContextT]` | Yes | Model request being processed. |
| `handler` | `Callable[[ModelRequest[ContextT]], ModelResponse[ResponseT]]` | Yes | Handler function to call with modified request. |

## Returns

`ModelResponse[ResponseT]`

Model response from handler.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/middleware/memory.py#L384)
