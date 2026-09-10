---
title: "FileUploadResponse"
description: "Result of a single file upload operation."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/FileUploadResponse"
category: "reference"
tags: [reference, deepagents, backends, protocol, fileuploadresponse]
---

# FileUploadResponse

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/FileUploadResponse)

Result of a single file upload operation.

The response is designed to allow partial success in batch operations.

The errors are standardized using `FileOperationError` literals for certain
recoverable conditions for use cases that involve LLMs performing
file operations.

## Signature

```python
FileUploadResponse(
    self,
    path: str,
    error: FileOperationError | str | None = None,
)
```

## Constructors

```python
__init__(
    self,
    path: str,
    error: FileOperationError | str | None = None,
) -> None
```

| Name | Type |
|------|------|
| `path` | `str` |
| `error` | `FileOperationError \| str \| None` |

## Properties

- `path`
- `error`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/backends/protocol.py#L97)
