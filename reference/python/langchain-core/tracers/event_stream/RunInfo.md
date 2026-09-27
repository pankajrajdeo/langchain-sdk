---
title: "RunInfo"
description: "Information about a run."
source: "https://reference.langchain.com/python/langchain-core/tracers/event_stream/RunInfo"
category: "reference"
tags: [reference, langchain-core, tracers, event_stream, runinfo]
---

# RunInfo

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/event_stream/RunInfo)

Information about a run.

This is used to keep track of the metadata associated with a run.

## Signature

```python
RunInfo()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    name: str,
    tags: list[str],
    metadata: dict[str, Any],
    run_type: str,
    inputs: NotRequired[Any],
    parent_run_id: UUID | None,
    tool_call_id: NotRequired[str | None],
)
```

| Name | Type |
|------|------|
| `name` | `str` |
| `tags` | `list[str]` |
| `metadata` | `dict[str, Any]` |
| `run_type` | `str` |
| `inputs` | `NotRequired[Any]` |
| `parent_run_id` | `UUID \| None` |
| `tool_call_id` | `NotRequired[str \| None]` |

## Properties

- `name`
- `tags`
- `metadata`
- `run_type`
- `inputs`
- `parent_run_id`
- `tool_call_id`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/tracers/event_stream.py#L58)
