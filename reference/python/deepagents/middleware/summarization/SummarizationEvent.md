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
    cutoff_message_id: NotRequired[str | None],
    summary_message: HumanMessage,
    file_path: str | None,
    created_at_index: NotRequired[int],
)
```

| Name | Type |
|------|------|
| `cutoff_index` | `int` |
| `cutoff_message_id` | `NotRequired[str \| None]` |
| `summary_message` | `HumanMessage` |
| `file_path` | `str \| None` |
| `created_at_index` | `NotRequired[int]` |

## Properties

- `cutoff_index`
- `cutoff_message_id`
- `summary_message`
- `file_path`
- `created_at_index`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/53e090968118f72f6dd3847d097607461a0fb5a8/libs/deepagents/deepagents/middleware/summarization.py#L158)
