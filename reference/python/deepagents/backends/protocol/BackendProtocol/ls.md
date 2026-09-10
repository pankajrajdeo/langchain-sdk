---
title: "ls"
description: "List all files in a directory with metadata."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/ls"
category: "reference"
tags: [reference, deepagents, backends, protocol, backendprotocol, ls]
---

# ls

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/ls)

List all files in a directory with metadata.

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
| `path` | `str` | Yes | Absolute path to the directory to list. Must start with `'/'`. |

## Returns

`LsResult`

`LsResult` with directory entries or error.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/backends/protocol.py#L436)
