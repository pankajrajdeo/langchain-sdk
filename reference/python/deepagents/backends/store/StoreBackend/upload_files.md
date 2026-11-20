---
title: "upload_files"
description: "Upload multiple files to the store."
source: "https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/upload_files"
category: "reference"
tags: [reference, deepagents, backends, store, storebackend, upload_files]
---

# upload_files

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/upload_files)

Upload multiple files to the store.

Content that is valid UTF-8 and contains no NUL bytes is stored as a
UTF-8 string. Everything else (images, PDFs, etc.) is stored as a
base64-encoded string.

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
| `files` | `list[tuple[str, bytes]]` | Yes | List of `(path, content)` tuples where content is bytes. |

## Returns

`list[FileUploadResponse]`

List of `FileUploadResponse` objects, one per input file.

Response order matches input order.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/5568767515b7edc6b106e92d3de4cc65886c1eca/libs/deepagents/deepagents/backends/store.py#L684)
