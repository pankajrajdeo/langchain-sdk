---
title: "write"
description: "Write content to a file, creating or overwriting it if it already exists."
source: "https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/write"
category: "reference"
tags: [reference, deepagents, backends, sandbox, basesandbox, write]
---

# write

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/write)

Write content to a file, creating or overwriting it if it already exists.

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
| `file_path` | `str` | Yes | Absolute path for the file. |
| `content` | `str` | Yes | UTF-8 text content to write. |

## Returns

`WriteResult`

`WriteResult` with `path` on success or `error` on failure.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/backends/sandbox.py#L1784)
