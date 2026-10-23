---
title: "SummarizationEvent"
description: "Represents a summarization event."
source: "https://reference.langchain.com/python/deepagents/middleware/summarization/SummarizationEvent"
category: "reference"
tags: [reference, deepagents, middleware, summarization, summarizationevent]
---

# SummarizationEvent

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/summarization/SummarizationEvent)

Represents a summarization event.

## Signature

```python
SummarizationEvent()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    cutoff_index: int,
    summary_message: HumanMessage,
    file_path: str | None,
    created_at_index: NotRequired[int],
)
```

| Name | Type |
|------|------|
| `cutoff_index` | `int` |
| `summary_message` | `HumanMessage` |
| `file_path` | `str \| None` |
| `created_at_index` | `NotRequired[int]` |

## Properties

- `cutoff_index`
- `summary_message`
- `file_path`
- `created_at_index`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/middleware/summarization.py#L149)
