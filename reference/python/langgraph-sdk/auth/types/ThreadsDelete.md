---
title: "ThreadsDelete"
description: "Parameters for deleting a thread."
source: "https://reference.langchain.com/python/langgraph-sdk/auth/types/ThreadsDelete"
category: "reference"
tags: [reference, langgraph-sdk, auth, types, threadsdelete]
---

# ThreadsDelete

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/auth/types/ThreadsDelete)

Parameters for deleting a thread.

Called for deletes to a thread, thread version, or run

## Signature

```python
ThreadsDelete()
```

## Extends

- `typing.TypedDict`

## Constructors

```python
__init__(
    thread_id: UUID,
    run_id: UUID | None,
)
```

| Name | Type |
|------|------|
| `thread_id` | `UUID` |
| `run_id` | `UUID \| None` |

## Properties

- `thread_id`
- `run_id`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/sdk-py/langgraph_sdk/auth/types.py#L502)
