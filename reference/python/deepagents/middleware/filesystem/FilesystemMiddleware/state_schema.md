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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/middleware/filesystem.py#L1972)
