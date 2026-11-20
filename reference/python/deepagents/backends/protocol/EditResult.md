---
title: "EditResult"
description: "Result from backend edit operations."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/EditResult"
category: "reference"
tags: [reference, deepagents, backends, protocol, editresult]
---

# EditResult

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/EditResult)

Result from backend `edit` operations.

## Signature

```python
EditResult(
    self,
    error: str | None = None,
    path: str | None = None,
    occurrences: int | None = None,
)
```

## Constructors

```python
__init__(
    self,
    error: str | None = None,
    path: str | None = None,
    occurrences: int | None = None,
) -> None
```

| Name | Type |
|------|------|
| `error` | `str \| None` |
| `path` | `str \| None` |
| `occurrences` | `int \| None` |

## Properties

- `error`
- `path`
- `occurrences`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/5568767515b7edc6b106e92d3de4cc65886c1eca/libs/deepagents/deepagents/backends/protocol.py#L294)
