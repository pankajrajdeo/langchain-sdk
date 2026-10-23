---
title: "ThreadTask"
description: "Represents a task within a thread."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/ThreadTask"
category: "reference"
tags: [reference, langgraph-sdk, schema, threadtask]
---

# ThreadTask

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/ThreadTask)

Represents a task within a thread.

## Signature

```python
ThreadTask()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    id: str,
    name: str,
    error: str | None,
    interrupts: list[Interrupt],
    checkpoint: Checkpoint | None,
    state: ThreadState | None,
    result: dict[str, Any] | None,
)
```

| Name | Type |
|------|------|
| `id` | `str` |
| `name` | `str` |
| `error` | `str \| None` |
| `interrupts` | `list[Interrupt]` |
| `checkpoint` | `Checkpoint \| None` |
| `state` | `ThreadState \| None` |
| `result` | `dict[str, Any] \| None` |

## Properties

- `id`
- `name`
- `error`
- `interrupts`
- `checkpoint`
- `state`
- `result`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/sdk-py/langgraph_sdk/schema.py#L323)
