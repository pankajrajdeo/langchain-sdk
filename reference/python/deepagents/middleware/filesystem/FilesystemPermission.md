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

With `FilesystemBackend` (directly or behind a `CompositeBackend` route),
rules are matched against both the requested path and its symlink-resolved
target; a deny on either blocks the call.

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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9b754bc914cc75c3f6d8c6e99353e81041b73bce/libs/deepagents/deepagents/middleware/filesystem.py#L375)
