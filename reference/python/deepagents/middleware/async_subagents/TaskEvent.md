---
title: "TaskEvent"
description: "How an async subagent's task ended or paused, as reported to the agent that started it."
source: "https://reference.langchain.com/python/deepagents/middleware/async_subagents/TaskEvent"
category: "reference"
tags: [reference, deepagents, middleware, async_subagents, taskevent]
---

# TaskEvent

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/async_subagents/TaskEvent)

How an async subagent's task ended or paused, as reported to the agent that started it.

A notification message carries it as notification metadata with source
`"async_subagent"`; read it with `get_notification_metadata(message).get("data")`.

`additional_kwargs["deepagents_notification"]` also carries it; that key is
deprecated.

!!! warning "Beta"

    This shape may change.

## Signature

```python
TaskEvent()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    task_id: str,
    agent_name: str,
    status: Literal['success', 'error', 'timeout', 'cancelled', 'waiting'],
    run_id: NotRequired[str],
)
```

| Name | Type |
|------|------|
| `task_id` | `str` |
| `agent_name` | `str` |
| `status` | `Literal['success', 'error', 'timeout', 'cancelled', 'waiting']` |
| `run_id` | `NotRequired[str]` |

## Properties

- `task_id`
- `agent_name`
- `status`
- `run_id`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0ec42441901968a75202a3ef365650eb280a473b/libs/deepagents/deepagents/middleware/async_subagents.py#L475)
