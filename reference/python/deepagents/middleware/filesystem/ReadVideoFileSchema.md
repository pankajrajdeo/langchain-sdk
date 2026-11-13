---
title: "ReadVideoFileSchema"
description: "Input schema for read_file when the optional video frame extraction is available."
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/ReadVideoFileSchema"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, readvideofileschema]
---

# ReadVideoFileSchema

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/filesystem/ReadVideoFileSchema)

Input schema for `read_file` when the optional video frame extraction is available.

Identical to `ReadFileSchema`; only the `offset`/`limit` descriptions differ
to document their video semantics (interpreted as seconds for video reads).

## Signature

```python
ReadVideoFileSchema()
```

## Extends

- `ReadFileSchema`

## Properties

- `offset`
- `limit`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0ec42441901968a75202a3ef365650eb280a473b/libs/deepagents/deepagents/middleware/filesystem.py#L1429)
