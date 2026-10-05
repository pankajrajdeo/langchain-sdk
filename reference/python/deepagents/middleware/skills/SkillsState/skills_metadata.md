---
title: "skills_metadata"
description: "List of loaded skill metadata from configured sources. Not propagated to parent agents."
source: "https://reference.langchain.com/python/deepagents/middleware/skills/SkillsState/skills_metadata"
category: "reference"
tags: [reference, deepagents, middleware, skills, skillsstate, skills_metadata]
---

# skills_metadata

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsState/skills_metadata)

List of loaded skill metadata from configured sources. Not propagated to parent agents.

Missing or `None` means not loaded; set to `None` to request a reload on the next run.
An empty list means loaded with no skills found.

## Signature

```python
skills_metadata: NotRequired[Annotated[list[SkillMetadata] | None, OmitFromOutput]]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/4394bcd00b8eb46e7c423939643a0dfcfb5d8773/libs/deepagents/deepagents/middleware/skills.py#L296)
