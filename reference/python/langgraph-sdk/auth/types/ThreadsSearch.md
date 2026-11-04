---
title: "ThreadsSearch"
description: "Parameters for searching threads."
source: "https://reference.langchain.com/python/langgraph-sdk/auth/types/ThreadsSearch"
category: "reference"
tags: [reference, langgraph-sdk, auth, types, threadssearch]
---

# ThreadsSearch

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/auth/types/ThreadsSearch)

Parameters for searching threads.

Called for searches to threads or runs.

## Signature

```python
ThreadsSearch()
```

## Extends

- `typing.TypedDict`

## Constructors

```python
__init__(
    metadata: MetadataInput,
    values: MetadataInput,
    status: ThreadStatus | None,
    limit: int,
    offset: int,
    ids: Sequence[UUID] | None,
    thread_id: UUID | None,
)
```

| Name | Type |
|------|------|
| `metadata` | `MetadataInput` |
| `values` | `MetadataInput` |
| `status` | `ThreadStatus \| None` |
| `limit` | `int` |
| `offset` | `int` |
| `ids` | `Sequence[UUID] \| None` |
| `thread_id` | `UUID \| None` |

## Properties

- `metadata`
- `values`
- `status`
- `limit`
- `offset`
- `ids`
- `thread_id`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5db97b9ccab6b8d9a5ab1e8f0bebea7c03a8708a/libs/sdk-py/langgraph_sdk/auth/types.py#L515)
