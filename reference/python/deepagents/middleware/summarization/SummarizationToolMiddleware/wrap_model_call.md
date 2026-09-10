---
title: "wrap_model_call"
description: "Inject a compact-tool usage nudge into the system prompt."
source: "https://reference.langchain.com/python/deepagents/middleware/summarization/SummarizationToolMiddleware/wrap_model_call"
category: "reference"
tags: [reference, deepagents, middleware, summarization, summarizationtoolmiddleware, wrap_model_call]
---

# wrap_model_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/summarization/SummarizationToolMiddleware/wrap_model_call)

Inject a compact-tool usage nudge into the system prompt.

This only updates prompt text so the model can decide whether to call
`compact_conversation` earlier in long sessions. It does not execute the
tool automatically.

## Signature

```python
wrap_model_call(
    self,
    request: ModelRequest,
    handler: Callable[[ModelRequest], ModelResponse],
) -> ModelResponse
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | `ModelRequest` | Yes | The model request to process. |
| `handler` | `Callable[[ModelRequest], ModelResponse]` | Yes | The handler to call with the modified request. |

## Returns

`ModelResponse`

The model response from the handler.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/middleware/summarization.py#L2123)
