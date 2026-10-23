---
title: "TruncateArgsSettings"
description: "Settings for truncating large tool-call arguments in older messages."
source: "https://reference.langchain.com/python/deepagents/middleware/summarization/TruncateArgsSettings"
category: "reference"
tags: [reference, deepagents, middleware, summarization, truncateargssettings]
---

# TruncateArgsSettings

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/summarization/TruncateArgsSettings)

Settings for truncating large tool-call arguments in older messages.

This is a lightweight, pre-summarization optimization that fires at a lower
token threshold than full conversation compaction. When triggered, only the
`args` values on `AIMessage.tool_calls` in messages *before* the keep window
are shortened — recent messages are left intact.

Typical large arguments include `write_file` content, `edit_file` patches,
and verbose `execute` outputs.

## Signature

```python
TruncateArgsSettings()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    trigger: ContextSize | None,
    keep: ContextSize,
    max_length: int,
    truncation_text: str,
)
```

| Name | Type |
|------|------|
| `trigger` | `ContextSize \| None` |
| `keep` | `ContextSize` |
| `max_length` | `int` |
| `truncation_text` | `str` |

## Properties

- `trigger`
- `keep`
- `max_length`
- `truncation_text`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/middleware/summarization.py#L185)
