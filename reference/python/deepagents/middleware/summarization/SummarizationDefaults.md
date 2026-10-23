---
title: "SummarizationDefaults"
description: "Default settings computed from model profile."
source: "https://reference.langchain.com/python/deepagents/middleware/summarization/SummarizationDefaults"
category: "reference"
tags: [reference, deepagents, middleware, summarization, summarizationdefaults]
---

# SummarizationDefaults

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/summarization/SummarizationDefaults)

Default settings computed from model profile.

## Signature

```python
SummarizationDefaults()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    trigger: ContextSize,
    keep: ContextSize,
    truncate_args_settings: TruncateArgsSettings,
)
```

| Name | Type |
|------|------|
| `trigger` | `ContextSize` |
| `keep` | `ContextSize` |
| `truncate_args_settings` | `TruncateArgsSettings` |

## Properties

- `trigger`
- `keep`
- `truncate_args_settings`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/middleware/summarization.py#L231)
