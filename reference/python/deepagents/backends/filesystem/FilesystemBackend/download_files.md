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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9ea3f1912abd8b7eecb504d78ef99fcf279bf561/libs/deepagents/deepagents/backends/filesystem.py#L1497)
