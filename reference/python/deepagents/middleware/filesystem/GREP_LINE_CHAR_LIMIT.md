---
title: "GREP_LINE_CHAR_LIMIT"
description: "Characters of a grep line shown to the model."
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/GREP_LINE_CHAR_LIMIT"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, grep_line_char_limit]
---

# GREP_LINE_CHAR_LIMIT

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/filesystem/GREP_LINE_CHAR_LIMIT)

Characters of a grep line shown to the model.

Longer lines (minified JSON, offloaded tool results) show a window around the
match instead, so one hit can't return the whole line.

## Signature

```python
GREP_LINE_CHAR_LIMIT = 2000
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0ec42441901968a75202a3ef365650eb280a473b/libs/deepagents/deepagents/middleware/filesystem.py#L828)
