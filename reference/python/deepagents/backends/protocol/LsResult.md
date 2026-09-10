---
title: "LsResult"
description: "Result from backend ls operations."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/LsResult"
category: "reference"
tags: [reference, deepagents, backends, protocol, lsresult]
---

# LsResult

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/LsResult)

Result from backend `ls` operations.

## Signature

```python
LsResult(
    self,
    error: str | None = None,
    entries: list[FileInfo] | None = None,
)
```

## Constructors

```python
__init__(
    self,
    error: str | None = None,
    entries: list[FileInfo] | None = None,
) -> None
```

| Name | Type |
|------|------|
| `error` | `str \| None` |
| `entries` | `list[FileInfo] \| None` |

## Properties

- `error`
- `entries`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/backends/protocol.py#L330)
