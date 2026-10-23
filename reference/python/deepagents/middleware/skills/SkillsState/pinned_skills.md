---
title: "pinned_skills"
description: "Names of skills to pin before the next model call."
source: "https://reference.langchain.com/python/deepagents/middleware/skills/SkillsState/pinned_skills"
category: "reference"
tags: [reference, deepagents, middleware, skills, skillsstate, pinned_skills]
---

# pinned_skills

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsState/pinned_skills)

Names of skills to pin before the next model call.

Each named skill's `SKILL.md`, without its frontmatter, is appended to the
conversation as its own `HumanMessage`. The message is a snapshot: editing the
file later doesn't change it, and naming the skill again appends a new copy.

Names only, matched exactly against `skills_metadata`. A name that isn't
loaded, or whose file can't be read, is skipped without an error. The key is
cleared once consumed, so a later run pins nothing unless it names skills
again. Writes in the same step add up, so parallel tool calls can each
pin skills.

## Signature

```python
pinned_skills: NotRequired[Annotated[list[str], OmitFromOutput, _append_skill_names]]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/middleware/skills.py#L357)
