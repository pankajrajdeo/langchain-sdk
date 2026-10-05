---
title: "GrepResult"
description: "Result from backend grep operations."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/GrepResult"
category: "reference"
tags: [reference, deepagents, backends, protocol, grepresult]
---

# GrepResult

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/GrepResult)

Result from backend `grep` operations.

## Signature

```python
GrepResult(
    self,
    error: str | None = None,
    matches: list[GrepMatch] | None = None,
    truncated: bool = False,
)
```

## Constructors

```python
__init__(
    self,
    error: str | None = None,
    matches: list[GrepMatch] | None = None,
    truncated: bool = False,
) -> None
```

| Name | Type |
|------|------|
| `error` | `str \| None` |
| `matches` | `list[GrepMatch] \| None` |
| `truncated` | `bool` |

## Properties

- `error`
- `matches`
- `truncated`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/4394bcd00b8eb46e7c423939643a0dfcfb5d8773/libs/deepagents/deepagents/backends/protocol.py#L343)
