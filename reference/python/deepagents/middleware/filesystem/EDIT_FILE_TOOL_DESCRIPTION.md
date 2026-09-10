---
title: "EDIT_FILE_TOOL_DESCRIPTION"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/EDIT_FILE_TOOL_DESCRIPTION"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, edit_file_tool_description]
---

# EDIT_FILE_TOOL_DESCRIPTION

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/filesystem/EDIT_FILE_TOOL_DESCRIPTION)

## Signature

```python
EDIT_FILE_TOOL_DESCRIPTION = 'Performs exact string replacements in files.\n\nUsage:\n- You must read the file before editing; this tool errors otherwise.\n- Preserve the exact indentation from the read output, and never include line-number prefixes in old_string or new_string.\n- Prefer editing an existing file over creating a new one.\n- Only use emojis if the user explicitly requests it.'
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/middleware/filesystem.py#L1283)
