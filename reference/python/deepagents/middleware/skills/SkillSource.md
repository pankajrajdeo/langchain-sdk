---
title: "SkillSource"
description: "Type Alias in deepagents"
source: "https://reference.langchain.com/python/deepagents/middleware/skills/SkillSource"
category: "reference"
tags: [reference, deepagents, middleware, skills, skillsource]
---

# SkillSource

> **Type Alias** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/skills/SkillSource)

A skill source: either a bare path or a `(path, label)` pair.

When only a path is given, the label is derived from the final path
component. Supply a tuple to override the default (e.g. to distinguish
user-scoped from project-scoped directories that share the same leaf
name). The label is rendered as `**{label} Skills**` in the system
prompt; do not include the trailing "Skills" yourself.

## Signature

```python
SkillSource = str | tuple[str, str]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/middleware/skills.py#L151)
