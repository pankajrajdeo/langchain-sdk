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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/53e090968118f72f6dd3847d097607461a0fb5a8/libs/deepagents/deepagents/backends/state.py#L354)
