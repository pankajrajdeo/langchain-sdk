---
title: "RunState"
description: "State of the run."
source: "https://reference.langchain.com/python/langchain-core/tracers/log_stream/RunState"
category: "reference"
tags: [reference, langchain-core, tracers, log_stream, runstate]
---

# RunState

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/log_stream/RunState)

State of the run.

## Signature

```python
RunState()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    id: str,
    streamed_output: list[Any],
    final_output: Any | None,
    name: str,
    type: str,
    logs: dict[str, LogEntry],
)
```

| Name | Type |
|------|------|
| `id` | `str` |
| `streamed_output` | `list[Any]` |
| `final_output` | `Any \| None` |
| `name` | `str` |
| `type` | `str` |
| `logs` | `dict[str, LogEntry]` |

## Properties

- `id`
- `streamed_output`
- `final_output`
- `name`
- `type`
- `logs`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/tracers/log_stream.py#L83)
