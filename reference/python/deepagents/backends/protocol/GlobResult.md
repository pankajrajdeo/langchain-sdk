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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/53e090968118f72f6dd3847d097607461a0fb5a8/libs/deepagents/deepagents/backends/protocol.py#L381)
