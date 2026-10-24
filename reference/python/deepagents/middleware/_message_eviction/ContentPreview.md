---
title: "ContentPreview"
description: "A rendered preview plus a record of what was left out to build it."
source: "https://reference.langchain.com/python/deepagents/middleware/_message_eviction/ContentPreview"
category: "reference"
tags: [reference, deepagents, middleware, message_eviction, contentpreview]
---

# ContentPreview

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/_message_eviction/ContentPreview)

A rendered preview plus a record of what was left out to build it.

The flags are reported by the code that built `text`, never inferred from
the rendered bytes — a literal `... [N lines truncated] ...` line in the
content would otherwise pass for a real marker. The two flags track
independent kinds of loss; a preview can have both, so check both.

## Signature

```python
ContentPreview(
    self,
    text: str,
    lines_omitted: bool,
    lines_clipped: bool,
)
```

## Constructors

```python
__init__(
    self,
    text: str,
    lines_omitted: bool,
    lines_clipped: bool,
) -> None
```

| Name | Type |
|------|------|
| `text` | `str` |
| `lines_omitted` | `bool` |
| `lines_clipped` | `bool` |

## Properties

- `text`
- `lines_omitted`
- `lines_clipped`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/middleware/_message_eviction.py#L64)
