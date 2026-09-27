---
title: "write"
description: "Write content to a file, creating it or overwriting it if it already exists."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/write"
category: "reference"
tags: [reference, deepagents, backends, protocol, backendprotocol, write]
---

# write

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/write)

Write content to a file, creating it or overwriting it if it already exists.

## Signature

```python
write(
    self,
    file_path: str,
    content: str,
) -> WriteResult
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `file_path` | `str` | Yes | Absolute path where the file should be written.  Must start with '/'. |
| `content` | `str` | Yes | String content to write to the file. |

## Returns

`WriteResult`

WriteResult

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/bb49cf50d3450a3bbebe8d25240cb7ef6379bd0d/libs/deepagents/deepagents/backends/protocol.py#L659)
