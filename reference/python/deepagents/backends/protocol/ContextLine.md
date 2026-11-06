---
title: "ContextLine"
description: "A non-matching line surrounding a grep match, used for context_lines."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/ContextLine"
category: "reference"
tags: [reference, deepagents, backends, protocol, contextline]
---

# ContextLine

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/ContextLine)

A non-matching line surrounding a grep match, used for `context_lines`.

## Signature

```python
ContextLine()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    line: int,
    text: str,
)
```

| Name | Type |
|------|------|
| `line` | `int` |
| `text` | `str` |

## Properties

- `line`
- `text`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9ea3f1912abd8b7eecb504d78ef99fcf279bf561/libs/deepagents/deepagents/backends/protocol.py#L149)
