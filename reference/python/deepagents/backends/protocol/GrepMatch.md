---
title: "GrepMatch"
description: "A single match from a grep search."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/GrepMatch"
category: "reference"
tags: [reference, deepagents, backends, protocol, grepmatch]
---

# GrepMatch

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/GrepMatch)

A single match from a grep search.

## Signature

```python
GrepMatch()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    path: str,
    line: int,
    text: str,
    context_before: NotRequired[list[ContextLine]],
    context_after: NotRequired[list[ContextLine]],
)
```

| Name | Type |
|------|------|
| `path` | `str` |
| `line` | `int` |
| `text` | `str` |
| `context_before` | `NotRequired[list[ContextLine]]` |
| `context_after` | `NotRequired[list[ContextLine]]` |

## Properties

- `path`
- `line`
- `text`
- `context_before`
- `context_after`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/backends/protocol.py#L159)
