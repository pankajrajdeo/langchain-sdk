---
title: "PriorityContext"
description: "Context passed to the @priority.assign function at the first run on a thread with no settings."
source: "https://reference.langchain.com/python/langgraph-sdk/priority/types/PriorityContext"
category: "reference"
tags: [reference, langgraph-sdk, priority, types, prioritycontext]
---

# PriorityContext

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/priority/types/PriorityContext)

Context passed to the `@priority.assign` function at the first run on a thread with no settings.

## Signature

```python
PriorityContext(
    self,
    user: BaseUser,
    permissions: Sequence[str],
    thread_id: str | None,
    thread_metadata: dict[str, typing.Any],
    assistant_id: str,
    graph_id: str,
    assistant_metadata: dict[str, typing.Any],
    run_metadata: dict[str, typing.Any],
    cron_id: str | None,
)
```

## Constructors

```python
__init__(
    self,
    user: BaseUser,
    permissions: Sequence[str],
    thread_id: str | None,
    thread_metadata: dict[str, typing.Any],
    assistant_id: str,
    graph_id: str,
    assistant_metadata: dict[str, typing.Any],
    run_metadata: dict[str, typing.Any],
    cron_id: str | None,
) -> None
```

| Name | Type |
|------|------|
| `user` | `BaseUser` |
| `permissions` | `Sequence[str]` |
| `thread_id` | `str \| None` |
| `thread_metadata` | `dict[str, typing.Any]` |
| `assistant_id` | `str` |
| `graph_id` | `str` |
| `assistant_metadata` | `dict[str, typing.Any]` |
| `run_metadata` | `dict[str, typing.Any]` |
| `cron_id` | `str \| None` |

## Properties

- `user`
- `permissions`
- `thread_id`
- `thread_metadata`
- `assistant_id`
- `graph_id`
- `assistant_metadata`
- `run_metadata`
- `cron_id`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5db97b9ccab6b8d9a5ab1e8f0bebea7c03a8708a/libs/sdk-py/langgraph_sdk/priority/types.py#L16)
