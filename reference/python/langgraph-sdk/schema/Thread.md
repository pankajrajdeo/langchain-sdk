---
title: "Thread"
description: "Represents a conversation thread."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/Thread"
category: "reference"
tags: [reference, langgraph-sdk, schema, thread]
---

# Thread

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/Thread)

Represents a conversation thread.

## Signature

```python
Thread()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    thread_id: str,
    created_at: datetime,
    updated_at: datetime,
    metadata: Json,
    status: ThreadStatus,
    values: Json,
    interrupts: dict[str, list[Interrupt]],
    extracted: NotRequired[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `thread_id` | `str` |
| `created_at` | `datetime` |
| `updated_at` | `datetime` |
| `metadata` | `Json` |
| `status` | `ThreadStatus` |
| `values` | `Json` |
| `interrupts` | `dict[str, list[Interrupt]]` |
| `extracted` | `NotRequired[dict[str, Any]]` |

## Properties

- `thread_id`
- `created_at`
- `updated_at`
- `metadata`
- `status`
- `values`
- `interrupts`
- `extracted`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/6b83b9b019c9b2680e4456dd6835d0fea27b9887/libs/sdk-py/langgraph_sdk/schema.py#L302)
