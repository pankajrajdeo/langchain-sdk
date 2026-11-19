---
title: "GlobResult"
description: "Result from backend glob operations."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/GlobResult"
category: "reference"
tags: [reference, deepagents, backends, protocol, globresult]
---

# GlobResult

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/GlobResult)

Result from backend `glob` operations.

## Signature

```python
GlobResult(
    self,
    error: str | None = None,
    matches: list[FileInfo] | None = None,
    truncated: bool = False,
    truncation_reason: GlobTruncationReason | None = None,
)
```

## Constructors

```python
__init__(
    self,
    error: str | None = None,
    matches: list[FileInfo] | None = None,
    truncated: bool = False,
    truncation_reason: GlobTruncationReason | None = None,
) -> None
```

| Name | Type |
|------|------|
| `error` | `str \| None` |
| `matches` | `list[FileInfo] \| None` |
| `truncated` | `bool` |
| `truncation_reason` | `GlobTruncationReason \| None` |

## Properties

- `error`
- `matches`
- `truncated`
- `truncation_reason`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9b754bc914cc75c3f6d8c6e99353e81041b73bce/libs/deepagents/deepagents/backends/protocol.py#L381)
