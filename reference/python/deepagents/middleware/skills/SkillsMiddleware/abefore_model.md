---
title: "abefore_model"
description: "Pin the skills named in pinned_skills before the model call (async)."
source: "https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/abefore_model"
category: "reference"
tags: [reference, deepagents, middleware, skills, skillsmiddleware, abefore_model]
---

# abefore_model

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/abefore_model)

Pin the skills named in `pinned_skills` before the model call (async).

Appends one message per named skill, in the order named, carrying its
`SKILL.md` without frontmatter. Names are matched against
`skills_metadata`; unknown or unreadable skills are skipped.

## Signature

```python
abefore_model(
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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/middleware/skills.py#L1282)
