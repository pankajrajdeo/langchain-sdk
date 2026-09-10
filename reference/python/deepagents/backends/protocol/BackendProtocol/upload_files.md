---
title: "upload_files"
description: "Upload multiple files to the sandbox."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/upload_files"
category: "reference"
tags: [reference, deepagents, backends, protocol, backendprotocol, upload_files]
---

# upload_files

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/upload_files)

Upload multiple files to the sandbox.

This API is designed to allow developers to use it either directly or by
exposing it to LLMs via custom tools.

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
| `files` | `list[tuple[str, bytes]]` | Yes | List of (path, content) tuples to upload. |

## Returns

`list[FileUploadResponse]`

List of `FileUploadResponse` objects, one per input file.

Response order matches input order (`response[i] for files[i]`).

Check the error field to determine success/failure per file.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/backends/protocol.py#L754)
