---
title: "max_count"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/GrepSchema/max_count"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, grepschema, max_count]
---

# max_count

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/filesystem/GrepSchema/max_count)

## Signature

```python
max_count: int | None = Field(default=None, gt=0, description='Optional cap on the total number of matches returned across all files. Leave unset to use the configured default. When the cap is hit, results are truncated and a note says so; narrow the pattern or path to see the rest.')
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9ea3f1912abd8b7eecb504d78ef99fcf279bf561/libs/deepagents/deepagents/middleware/filesystem.py#L1498)
