---
title: "FilesystemPermission"
description: "A single access rule for filesystem operations."
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemPermission"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, filesystempermission]
---

# FilesystemPermission

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemPermission)

A single access rule for filesystem operations.

## Signature

```python
FilesystemPermission(
    self,
    operations: list[FilesystemOperation],
    paths: list[str],
    mode: Literal['allow', 'deny', 'interrupt'] = 'allow',
)
```

## Constructors

```python
__init__(
    self,
    operations: list[FilesystemOperation],
    paths: list[str],
    mode: Literal['allow', 'deny', 'interrupt'] = 'allow',
) -> None
```

| Name | Type |
|------|------|
| `operations` | `list[FilesystemOperation]` |
| `paths` | `list[str]` |
| `mode` | `Literal['allow', 'deny', 'interrupt']` |

## Properties

- `operations`
- `paths`
- `mode`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/bb49cf50d3450a3bbebe8d25240cb7ef6379bd0d/libs/deepagents/deepagents/middleware/filesystem.py#L353)
