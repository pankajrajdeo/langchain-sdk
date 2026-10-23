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

A notification message carries it in `additional_kwargs["deepagents_notification"]`,
so apps can tell these messages from the user's.

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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/middleware/async_subagents.py#L458)
