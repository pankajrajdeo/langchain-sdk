---
title: "before_model"
description: "Pin the skills named in pinned_skills before the model call (synchronous)."
source: "https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/before_model"
category: "reference"
tags: [reference, deepagents, middleware, skills, skillsmiddleware, before_model]
---

# before_model

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/before_model)

Pin the skills named in `pinned_skills` before the model call (synchronous).

Appends one message per named skill, in the order named, carrying its
`SKILL.md` without frontmatter. Names are matched against
`skills_metadata`; unknown or unreadable skills are skipped.

## Signature

```python
before_model(
    self,
    state: SkillsState,
    runtime: Runtime[ContextT],
) -> dict[str, Any] | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `state` | `SkillsState` | Yes | Current agent state. |
| `runtime` | `Runtime[ContextT]` | Yes | Runtime context. |

## Returns

`dict[str, Any] | None`

State update appending the skills' messages and clearing
`pinned_skills`, or `None` if no skills are named.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/middleware/skills.py#L1260)
