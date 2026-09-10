---
title: "download_files"
description: "Download multiple files from state."
source: "https://reference.langchain.com/python/deepagents/backends/state/StateBackend/download_files"
category: "reference"
tags: [reference, deepagents, backends, state, statebackend, download_files]
---

# download_files

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/state/StateBackend/download_files)

Download multiple files from state.

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
| `paths` | `list[str]` | Yes | List of file paths to download |

## Returns

`list[FileDownloadResponse]`

List of `FileDownloadResponse` objects, one per input path

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/backends/state.py#L349)
