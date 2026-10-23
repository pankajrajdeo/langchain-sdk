---
title: "modify_request"
description: "Inject skills documentation into a model request's system message."
source: "https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/modify_request"
category: "reference"
tags: [reference, deepagents, middleware, skills, skillsmiddleware, modify_request]
---

# modify_request

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/modify_request)

Inject skills documentation into a model request's system message.

## Signature

```python
modify_request(
    self,
    request: ModelRequest[ContextT],
) -> ModelRequest[ContextT]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | `ModelRequest[ContextT]` | Yes | Model request to modify |

## Returns

`ModelRequest[ContextT]`

New model request with skills documentation injected into system message

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/middleware/skills.py#L1138)
