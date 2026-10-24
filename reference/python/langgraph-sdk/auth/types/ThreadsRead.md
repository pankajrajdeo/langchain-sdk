---
title: "ThreadsRead"
description: "Parameters for reading thread state or run information."
source: "https://reference.langchain.com/python/langgraph-sdk/auth/types/ThreadsRead"
category: "reference"
tags: [reference, langgraph-sdk, auth, types, threadsread]
---

# ThreadsRead

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/auth/types/ThreadsRead)

Parameters for reading thread state or run information.

This type is used in three contexts:
1. Reading thread, thread version, or thread state information: Only thread_id is provided
2. Reading run information: Both thread_id and run_id are provided

## Signature

```python
ThreadsRead()
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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/6b83b9b019c9b2680e4456dd6835d0fea27b9887/libs/sdk-py/langgraph_sdk/auth/types.py#L470)
