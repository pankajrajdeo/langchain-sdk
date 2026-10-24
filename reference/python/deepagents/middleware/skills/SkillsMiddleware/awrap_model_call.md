---
title: "awrap_model_call"
description: "Inject skills documentation into the system prompt and disclose read skills' tools (async version)."
source: "https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/awrap_model_call"
category: "reference"
tags: [reference, deepagents, middleware, skills, skillsmiddleware, awrap_model_call]
---

# awrap_model_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/awrap_model_call)

Inject skills documentation into the system prompt and disclose read skills' tools (async version).

## Signature

```python
awrap_model_call(
    self,
    request: ModelRequest[ContextT],
    handler: Callable[[ModelRequest[ContextT]], Awaitable[ModelResponse[ResponseT]]],
) -> ModelResponse[ResponseT] | ExtendedModelResponse[ResponseT]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | `ModelRequest[ContextT]` | Yes | Model request being processed |
| `handler` | `Callable[[ModelRequest[ContextT]], Awaitable[ModelResponse[ResponseT]]]` | Yes | Async handler function to call with modified request |

## Returns

`ModelResponse[ResponseT] | ExtendedModelResponse[ResponseT]`

Model response from handler, with the skill tools it disclosed recorded
in state.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/middleware/skills.py#L1344)
