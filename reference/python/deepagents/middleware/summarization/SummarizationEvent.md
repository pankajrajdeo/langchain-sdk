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
)
```

| Name | Type |
|------|------|
| `cutoff_index` | `int` |
| `summary_message` | `HumanMessage` |
| `file_path` | `str \| None` |

## Properties

- `cutoff_index`
- `summary_message`
- `file_path`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/4394bcd00b8eb46e7c423939643a0dfcfb5d8773/libs/deepagents/deepagents/middleware/summarization.py#L142)
