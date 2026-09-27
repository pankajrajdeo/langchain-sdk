---
title: "TasksStreamPart"
description: "Stream part emitted for stream_mode=\"tasks\"."
source: "https://reference.langchain.com/python/langgraph/types/TasksStreamPart"
category: "reference"
tags: [reference, langgraph, types, tasksstreampart]
---

# TasksStreamPart

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/TasksStreamPart)

Stream part emitted for `stream_mode="tasks"`.

For task start events, `data` is a `TaskPayload` with `id`, `name`,
`input`, and `triggers` keys.

For task result events, `data` is a `TaskResultPayload` with `id`,
`name`, `error`, `interrupts`, and `result` keys.

## Signature

```python
TasksStreamPart()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['tasks'],
    ns: tuple[str, ...],
    data: TaskPayload | TaskResultPayload,
)
```

| Name | Type |
|------|------|
| `type` | `Literal['tasks']` |
| `ns` | `tuple[str, ...]` |
| `data` | `TaskPayload \| TaskResultPayload` |

## Properties

- `type`
- `ns`
- `data`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/types.py#L329)
