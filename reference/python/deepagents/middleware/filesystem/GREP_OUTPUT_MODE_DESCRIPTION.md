---
title: "GREP_OUTPUT_MODE_DESCRIPTION"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/GREP_OUTPUT_MODE_DESCRIPTION"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, grep_output_mode_description]
---

# GREP_OUTPUT_MODE_DESCRIPTION

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/filesystem/GREP_OUTPUT_MODE_DESCRIPTION)

## Signature

```python
GREP_OUTPUT_MODE_DESCRIPTION = "Shape of the returned text. 'files_with_matches' (default): newline-separated matching file paths. 'content': matching lines grouped by file under a '<path>:' header, each line indented and formatted '<line_number>: <line text>' (only the matched line, no surrounding context). 'count': one '<path>: <match_count>' line per file."
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/middleware/filesystem.py#L1112)
