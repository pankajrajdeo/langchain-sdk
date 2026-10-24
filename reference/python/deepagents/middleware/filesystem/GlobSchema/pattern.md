---
title: "pattern"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/GlobSchema/pattern"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, globschema, pattern]
---

# pattern

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/filesystem/GlobSchema/pattern)

## Signature

```python
pattern: str = Field(description="Glob pattern to match files (e.g., '*.py', '**/*.py', '/subdir/**/*.md'). A pattern without '/' matches the file name at any depth; a pattern containing '/' matches the search-root-relative path; a leading '/' anchors to the search root ('/*.py' matches only top-level files). Leading-dot names are excluded unless the pattern segment starts with '.', so prefer the bare form '*.py' over '**/*.py' -- '**' will not descend into dot-directories like '.github'.")
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/middleware/filesystem.py#L1436)
