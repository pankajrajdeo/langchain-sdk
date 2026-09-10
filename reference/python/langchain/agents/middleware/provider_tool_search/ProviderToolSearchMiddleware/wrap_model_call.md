---
title: "wrap_model_call"
description: "Defer tools before invoking the model."
source: "https://reference.langchain.com/python/langchain/agents/middleware/provider_tool_search/ProviderToolSearchMiddleware/wrap_model_call"
category: "reference"
tags: [reference, langchain, agents, middleware, provider_tool_search, providertoolsearchmiddleware, wrap_model_call]
---

# wrap_model_call

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/provider_tool_search/ProviderToolSearchMiddleware/wrap_model_call)

Defer tools before invoking the model.

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
| `request` | `ModelRequest[ContextT]` | Yes | Model request to execute. |
| `handler` | `Callable[[ModelRequest[ContextT]], ModelResponse[ResponseT]]` | Yes | Callback that executes the model request. |

## Returns

`ModelResponse[ResponseT] | AIMessage`

The model call result.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/middleware/provider_tool_search.py#L156)
