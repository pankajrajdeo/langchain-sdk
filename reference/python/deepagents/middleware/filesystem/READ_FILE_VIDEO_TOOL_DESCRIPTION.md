---
title: "READ_FILE_VIDEO_TOOL_DESCRIPTION"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/READ_FILE_VIDEO_TOOL_DESCRIPTION"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, read_file_video_tool_description]
---

# READ_FILE_VIDEO_TOOL_DESCRIPTION

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/filesystem/READ_FILE_VIDEO_TOOL_DESCRIPTION)

## Signature

```python
READ_FILE_VIDEO_TOOL_DESCRIPTION = _READ_FILE_TOOL_DESCRIPTION_TEMPLATE.format(first_line='For text files, by default it reads up to 100 lines starting from the beginning of the file', multimodal_bullets=f'{_IMAGE_PDF_PAGINATION_BULLET}\n- For videos, `offset`/`limit` are interpreted as seconds (default window 100 s; sampled at a fixed rate). Use smaller windows when you need more temporal detail.')
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/middleware/filesystem.py#L1517)
