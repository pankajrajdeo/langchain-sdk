---
title: "SkillsStateUpdate"
description: "State update for the skills middleware."
source: "https://reference.langchain.com/python/deepagents/middleware/skills/SkillsStateUpdate"
category: "reference"
tags: [reference, deepagents, middleware, skills, skillsstateupdate]
---

# SkillsStateUpdate

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsStateUpdate)

State update for the skills middleware.

## Signature

```python
SkillsStateUpdate()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    skills_metadata: list[SkillMetadata],
    skills_load_errors: NotRequired[list[str]],
)
```

| Name | Type |
|------|------|
| `skills_metadata` | `list[SkillMetadata]` |
| `skills_load_errors` | `NotRequired[list[str]]` |

## Properties

- `skills_metadata`
- `skills_load_errors`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/4394bcd00b8eb46e7c423939643a0dfcfb5d8773/libs/deepagents/deepagents/middleware/skills.py#L307)
