---
title: "ls"
description: "List files and directories in the specified directory (non-recursive)."
source: "https://reference.langchain.com/python/deepagents/backends/state/StateBackend/ls"
category: "reference"
tags: [reference, deepagents, backends, state, statebackend, ls]
---

# ls

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/state/StateBackend/ls)

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
| `path` | `str` | Yes | Absolute path to directory. |

## Returns

`LsResult`

List of `FileInfo`-like dicts for files and directories directly in the directory.

Directories have a trailing `/` in their path and `is_dir=True`.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/bb49cf50d3450a3bbebe8d25240cb7ef6379bd0d/libs/deepagents/deepagents/backends/state.py#L125)
