---
title: "write"
description: "Create a new file, routing to appropriate backend."
source: "https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/write"
category: "reference"
tags: [reference, deepagents, backends, composite, compositebackend, write]
---

# write

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/write)

Create a new file, routing to appropriate backend.

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
| `file_path` | `str` | Yes | Absolute file path. |
| `content` | `str` | Yes | File content as a string. |

## Returns

`WriteResult`

Success message or `Command` object, or error if file already exists.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/backends/composite.py#L708)
