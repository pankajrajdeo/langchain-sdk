---
title: "upload_files"
description: "Upload multiple files, batching by backend for efficiency."
source: "https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/upload_files"
category: "reference"
tags: [reference, deepagents, backends, composite, compositebackend, upload_files]
---

# upload_files

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/upload_files)

Upload multiple files, batching by backend for efficiency.

Groups files by their target backend, calls each backend's
`upload_files` once with all files for that backend, then merges
results in original order.

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
| `files` | `list[tuple[str, bytes]]` | Yes | List of `(path, content)` tuples to upload. |

## Returns

`list[FileUploadResponse]`

List of `FileUploadResponse` objects, one per input file.

Response order matches input order.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/backends/composite.py#L877)
