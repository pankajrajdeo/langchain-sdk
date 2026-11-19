---
title: "upload_files"
description: "Upload multiple files to state."
source: "https://reference.langchain.com/python/deepagents/backends/state/StateBackend/upload_files"
category: "reference"
tags: [reference, deepagents, backends, state, statebackend, upload_files]
---

# upload_files

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/state/StateBackend/upload_files)

Upload multiple files to state.

## Signature

```python
upload_files(
    self,
    files: list[tuple[str, bytes]],
) -> list[FileUploadResponse]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `files` | `list[tuple[str, bytes]]` | Yes | List of `(path, content)` tuples to upload |

## Returns

`list[FileUploadResponse]`

List of `FileUploadResponse` objects, one per input file

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9b754bc914cc75c3f6d8c6e99353e81041b73bce/libs/deepagents/deepagents/backends/state.py#L326)
