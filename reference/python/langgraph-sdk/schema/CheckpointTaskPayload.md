---
title: "CheckpointTaskPayload"
description: "A task entry within a CheckpointPayload."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/CheckpointTaskPayload"
category: "reference"
tags: [reference, langgraph-sdk, schema, checkpointtaskpayload]
---

# CheckpointTaskPayload

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/CheckpointTaskPayload)

A task entry within a `CheckpointPayload`.

The keys present depend on the task's state:

- **Error:** `id`, `name`, `error`, `state`
- **Has result:** `id`, `name`, `result`, `interrupts`, `state`
- **Pending:** `id`, `name`, `interrupts`, `state`

## Signature

```python
CheckpointTaskPayload()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    id: str,
    name: str,
    error: NotRequired[str],
    result: NotRequired[Any],
    interrupts: NotRequired[list[dict[str, Any]]],
    state: dict[str, Any] | None,
)
```

| Name | Type |
|------|------|
| `id` | `str` |
| `name` | `str` |
| `error` | `NotRequired[str]` |
| `result` | `NotRequired[Any]` |
| `interrupts` | `NotRequired[list[dict[str, Any]]]` |
| `state` | `dict[str, Any] \| None` |

## Properties

- `id`
- `name`
- `error`
- `result`
- `interrupts`
- `state`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/6b83b9b019c9b2680e4456dd6835d0fea27b9887/libs/sdk-py/langgraph_sdk/schema.py#L647)
