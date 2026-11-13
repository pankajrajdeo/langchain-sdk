---
title: "FileOperationError"
description: "Standardized error codes for file upload/download operations."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/FileOperationError"
category: "reference"
tags: [reference, deepagents, backends, protocol, fileoperationerror]
---

# FileOperationError

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/FileOperationError)

Standardized error codes for file upload/download operations.

These represent common, recoverable errors that an LLM can understand and
potentially fix:

- `file_not_found`: The requested file doesn't exist (download)
- `permission_denied`: Access denied for the operation
- `is_directory`: Attempted to download a directory as a file
- `invalid_path`: Path syntax is malformed or contains invalid characters

## Signature

```python
FileOperationError = Literal['file_not_found', 'permission_denied', 'is_directory', 'invalid_path']
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0ec42441901968a75202a3ef365650eb280a473b/libs/deepagents/deepagents/backends/protocol.py#L39)
