---
title: "compatibility"
description: "Environment requirements."
source: "https://reference.langchain.com/python/deepagents/middleware/skills/SkillMetadata/compatibility"
category: "reference"
tags: [reference, deepagents, middleware, skills, skillmetadata, compatibility]
---

# compatibility

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/skills/SkillMetadata/compatibility)

Environment requirements.

Constraints per Agent Skills specification:

- 1-500 characters if provided
- Should only be included if there are specific compatibility requirements
- Can indicate intended product, required packages, etc.

## Signature

```python
compatibility: str | None
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/bb49cf50d3450a3bbebe8d25240cb7ef6379bd0d/libs/deepagents/deepagents/middleware/skills.py#L264)
