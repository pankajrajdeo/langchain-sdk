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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/53e090968118f72f6dd3847d097607461a0fb5a8/libs/deepagents/deepagents/backends/protocol.py#L277)
