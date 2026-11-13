---
title: "write"
description: "Write content to a file, creating it or overwriting it if it already exists."
source: "https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/write"
category: "reference"
tags: [reference, deepagents, backends, filesystem, filesystembackend, write]
---

# write

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/write)

Write content to a file, creating it or overwriting it if it already exists.

## Signature

```python
write(
    self,
    file_path: str,
    content: str,
) -> WriteResult
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `file_path` | `str` | Yes | Path where the file will be written. |
| `content` | `str` | Yes | Text content to write to the file. |

## Returns

`WriteResult`

`WriteResult` with path on success, or error message on write failure.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0ec42441901968a75202a3ef365650eb280a473b/libs/deepagents/deepagents/backends/filesystem.py#L505)
