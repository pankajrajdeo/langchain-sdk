---
title: "ThreadState"
description: "Represents the state of a thread."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/ThreadState"
category: "reference"
tags: [reference, langgraph-sdk, schema, threadstate]
---

# ThreadState

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/ThreadState)

Represents the state of a thread.

## Signature

```python
ThreadState()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    values: list[dict] | dict[str, Any],
    next: Sequence[str],
    checkpoint: Checkpoint,
    metadata: Json,
    created_at: str | None,
    parent_checkpoint: Checkpoint | None,
    tasks: Sequence[ThreadTask],
    interrupts: list[Interrupt],
)
```

| Name | Type |
|------|------|
| `values` | `list[dict] \| dict[str, Any]` |
| `next` | `Sequence[str]` |
| `checkpoint` | `Checkpoint` |
| `metadata` | `Json` |
| `created_at` | `str \| None` |
| `parent_checkpoint` | `Checkpoint \| None` |
| `tasks` | `Sequence[ThreadTask]` |
| `interrupts` | `list[Interrupt]` |

## Properties

- `values`
- `next`
- `checkpoint`
- `metadata`
- `created_at`
- `parent_checkpoint`
- `tasks`
- `interrupts`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/sdk-py/langgraph_sdk/schema.py#L335)
