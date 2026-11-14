---
title: "download_files"
description: "Download multiple files from the filesystem."
source: "https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/download_files"
category: "reference"
tags: [reference, deepagents, backends, filesystem, filesystembackend, download_files]
---

# download_files

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/download_files)

Download multiple files from the filesystem.

A path that is not a regular file, such as a FIFO or a device, fails
with `file_not_found`, as `read` reports it.

## Signature

```python
download_files(
    self,
    paths: list[str],
) -> list[FileDownloadResponse]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `paths` | `list[str]` | Yes | List of file paths to download. |

## Returns

`list[FileDownloadResponse]`

List of `FileDownloadResponse` objects, one per input path.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/c858b3641b13fb3f40fe3a12515517b81fb8a744/libs/deepagents/deepagents/backends/filesystem.py#L1499)
