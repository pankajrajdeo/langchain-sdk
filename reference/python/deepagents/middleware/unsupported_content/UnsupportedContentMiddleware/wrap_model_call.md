---
title: "wrap_model_call"
description: "Filter unsupported input blocks, then invoke the model."
source: "https://reference.langchain.com/python/deepagents/middleware/unsupported_content/UnsupportedContentMiddleware/wrap_model_call"
category: "reference"
tags: [reference, deepagents, middleware, unsupported_content, unsupportedcontentmiddleware, wrap_model_call]
---

# wrap_model_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/unsupported_content/UnsupportedContentMiddleware/wrap_model_call)

Filter unsupported input blocks, then invoke the model.

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
| `request` | `ModelRequest[ContextT]` | Yes | Model request to execute. |
| `handler` | `Callable[[ModelRequest[ContextT]], ModelResponse[ResponseT]]` | Yes | Callback that executes the model request. |

## Returns

`ModelResponse[ResponseT]`

The result of invoking the handler.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/bb49cf50d3450a3bbebe8d25240cb7ef6379bd0d/libs/deepagents/deepagents/middleware/unsupported_content.py#L177)
