---
title: "Run"
description: "Represents a single execution run."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/Run"
category: "reference"
tags: [reference, langgraph-sdk, schema, run]
---

# Run

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/Run)

Represents a single execution run.

## Signature

```python
Run()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    run_id: str,
    thread_id: str,
    assistant_id: str,
    created_at: datetime,
    updated_at: datetime,
    status: RunStatus,
    metadata: Json,
    multitask_strategy: MultitaskStrategy,
    cancel_reason: NotRequired[str | None],
)
```

| Name | Type |
|------|------|
| `run_id` | `str` |
| `thread_id` | `str` |
| `assistant_id` | `str` |
| `created_at` | `datetime` |
| `updated_at` | `datetime` |
| `status` | `RunStatus` |
| `metadata` | `Json` |
| `multitask_strategy` | `MultitaskStrategy` |
| `cancel_reason` | `NotRequired[str \| None]` |

## Properties

- `run_id`
- `thread_id`
- `assistant_id`
- `created_at`
- `updated_at`
- `status`
- `metadata`
- `multitask_strategy`
- `cancel_reason`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/sdk-py/langgraph_sdk/schema.py#L364)
