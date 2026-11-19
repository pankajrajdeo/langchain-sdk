---
title: "state_schema"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware/state_schema"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, filesystemmiddleware, state_schema]
---

# state_schema

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware/state_schema)

## Signature

```python
state_schema: type[FilesystemState] = cast('type[FilesystemState]', _FilesystemBlobPayloadState if _uses_state_backend(self.backend) else _BlobPayloadState)
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9b754bc914cc75c3f6d8c6e99353e81041b73bce/libs/deepagents/deepagents/middleware/filesystem.py#L2070)
