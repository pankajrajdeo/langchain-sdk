---
title: "awrap_model_call"
description: "Filter unsupported input blocks, then invoke the model."
source: "https://reference.langchain.com/python/deepagents/middleware/unsupported_content/UnsupportedContentMiddleware/awrap_model_call"
category: "reference"
tags: [reference, deepagents, middleware, unsupported_content, unsupportedcontentmiddleware, awrap_model_call]
---

# awrap_model_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/unsupported_content/UnsupportedContentMiddleware/awrap_model_call)

Filter unsupported input blocks, then invoke the model.

## Signature

```python
awrap_model_call(
    self,
    request: ModelRequest[ContextT],
    handler: Callable[[ModelRequest[ContextT]], Awaitable[ModelResponse[ResponseT]]],
) -> ModelResponse[ResponseT]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | `ModelRequest[ContextT]` | Yes | Model request to execute. |
| `handler` | `Callable[[ModelRequest[ContextT]], Awaitable[ModelResponse[ResponseT]]]` | Yes | Async callback that executes the model request. |

## Returns

`ModelResponse[ResponseT]`

The result of invoking the handler.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/4394bcd00b8eb46e7c423939643a0dfcfb5d8773/libs/deepagents/deepagents/middleware/unsupported_content.py#L193)
