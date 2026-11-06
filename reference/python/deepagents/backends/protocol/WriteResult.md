---
title: "WriteResult"
description: "Result from backend write operations."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/WriteResult"
category: "reference"
tags: [reference, deepagents, backends, protocol, writeresult]
---

# WriteResult

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/WriteResult)

Result from backend `write` operations.

## Signature

```python
WriteResult(
    self,
    error: str | None = None,
    path: str | None = None,
)
```

## Constructors

```python
__init__(
    self,
    error: str | None = None,
    path: str | None = None,
) -> None
```

| Name | Type |
|------|------|
| `error` | `str \| None` |
| `path` | `str \| None` |

## Properties

- `error`
- `path`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9ea3f1912abd8b7eecb504d78ef99fcf279bf561/libs/deepagents/deepagents/backends/protocol.py#L277)
