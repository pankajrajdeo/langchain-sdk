---
title: "TaskPayload"
description: "Payload for a task start event."
source: "https://reference.langchain.com/python/langgraph/types/TaskPayload"
category: "reference"
tags: [reference, langgraph, types, taskpayload]
---

# TaskPayload

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/TaskPayload)

Payload for a task start event.

## Signature

```python
TaskPayload()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    id: str,
    name: str,
    input: Any,
    triggers: list[str],
    metadata: NotRequired[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `id` | `str` |
| `name` | `str` |
| `input` | `Any` |
| `triggers` | `list[str]` |
| `metadata` | `NotRequired[dict[str, Any]]` |

## Properties

- `id`
- `name`
- `input`
- `triggers`
- `metadata`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/types.py#L153)
