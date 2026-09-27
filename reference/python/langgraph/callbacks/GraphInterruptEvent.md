---
title: "GraphInterruptEvent"
description: "Graph lifecycle event emitted when execution pauses for interrupts."
source: "https://reference.langchain.com/python/langgraph/callbacks/GraphInterruptEvent"
category: "reference"
tags: [reference, langgraph, callbacks, graphinterruptevent]
---

# GraphInterruptEvent

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/callbacks/GraphInterruptEvent)

Graph lifecycle event emitted when execution pauses for interrupts.

## Signature

```python
GraphInterruptEvent(
    self,
    run_id: UUID | None,
    status: GraphLifecycleStatus,
    checkpoint_id: str,
    checkpoint_ns: tuple[str, ...],
    interrupts: tuple[Interrupt, ...],
)
```

## Constructors

```python
__init__(
    self,
    run_id: UUID | None,
    status: GraphLifecycleStatus,
    checkpoint_id: str,
    checkpoint_ns: tuple[str, ...],
    interrupts: tuple[Interrupt, ...],
) -> None
```

| Name | Type |
|------|------|
| `run_id` | `UUID \| None` |
| `status` | `GraphLifecycleStatus` |
| `checkpoint_id` | `str` |
| `checkpoint_ns` | `tuple[str, ...]` |
| `interrupts` | `tuple[Interrupt, ...]` |

## Properties

- `run_id`
- `status`
- `checkpoint_id`
- `checkpoint_ns`
- `interrupts`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/callbacks.py#L42)
