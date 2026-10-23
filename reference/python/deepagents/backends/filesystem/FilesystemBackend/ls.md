---
title: "ls"
description: "List files and directories in the specified directory (non-recursive)."
source: "https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/ls"
category: "reference"
tags: [reference, deepagents, backends, filesystem, filesystembackend, ls]
---

# ls

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/ls)

List files and directories in the specified directory (non-recursive).

## Signature

```python
ls(
    self,
    path: str,
) -> LsResult
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `str` | Yes | Absolute directory path to list files from. |

## Returns

`LsResult`

`LsResult` with `entries` listing files and directories directly in the
directory on success.

Directories have a trailing `/` in their path and `is_dir=True`.

Missing paths set `error` to `Path '<path>': path_not_found`
with `entries=None`.

File paths set `error` to `Path '<path>': not_a_directory`
with `entries=None`.

Empty directories return `error=None` and `entries=[]`.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/backends/filesystem.py#L285)
