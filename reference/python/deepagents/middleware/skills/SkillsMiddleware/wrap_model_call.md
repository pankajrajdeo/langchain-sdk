---
title: "wrap_model_call"
description: "Inject skills documentation into the system prompt and disclose read skills' tools."
source: "https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/wrap_model_call"
category: "reference"
tags: [reference, deepagents, middleware, skills, skillsmiddleware, wrap_model_call]
---

# wrap_model_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/wrap_model_call)

Inject skills documentation into the system prompt and disclose read skills' tools.

## Signature

```python
wrap_model_call(
    self,
    request: ModelRequest[ContextT],
    handler: Callable[[ModelRequest[ContextT]], ModelResponse[ResponseT]],
) -> ModelResponse[ResponseT] | ExtendedModelResponse[ResponseT]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | `ModelRequest[ContextT]` | Yes | Model request being processed |
| `handler` | `Callable[[ModelRequest[ContextT]], ModelResponse[ResponseT]]` | Yes | Handler function to call with modified request |

## Returns

`ModelResponse[ResponseT] | ExtendedModelResponse[ResponseT]`

Model response from handler, with the skill tools it disclosed recorded
in state.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/middleware/skills.py#L1322)
