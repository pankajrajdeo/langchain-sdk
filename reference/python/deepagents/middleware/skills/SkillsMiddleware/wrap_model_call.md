---
title: "wrap_model_call"
description: "Inject skills documentation into the system prompt."
source: "https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/wrap_model_call"
category: "reference"
tags: [reference, deepagents, middleware, skills, skillsmiddleware, wrap_model_call]
---

# wrap_model_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/wrap_model_call)

Inject skills documentation into the system prompt.

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
| `request` | `ModelRequest[ContextT]` | Yes | Model request being processed |
| `handler` | `Callable[[ModelRequest[ContextT]], ModelResponse[ResponseT]]` | Yes | Handler function to call with modified request |

## Returns

`ModelResponse[ResponseT]`

Model response from handler

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/middleware/skills.py#L1023)
