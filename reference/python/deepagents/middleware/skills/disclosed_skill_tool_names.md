---
title: "disclosed_skill_tool_names"
description: "Return the names of the skill tools disclosed to the latest model call."
source: "https://reference.langchain.com/python/deepagents/middleware/skills/disclosed_skill_tool_names"
category: "reference"
tags: [reference, deepagents, middleware, skills, disclosed_skill_tool_names]
---

# disclosed_skill_tool_names

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/skills/disclosed_skill_tool_names)

Return the names of the skill tools disclosed to the latest model call.

Use it in middleware that gates tool calls itself, so the gate admits the
skill tools the model has been shown. The agent's own deferred tools aren't
included, even when a skill disclosed them.

## Signature

```python
disclosed_skill_tool_names(
    state: Mapping[str, object],
) -> frozenset[str]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `state` | `Mapping[str, object]` | Yes | The agent state, such as `request.state` in `wrap_tool_call`. |

## Returns

`frozenset[str]`

The disclosed skill tools' names, or an empty set if there are none.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/middleware/skills.py#L1416)
