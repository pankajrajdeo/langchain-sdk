---
title: "TaskResultPayload"
description: "Payload for a task result event."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/TaskResultPayload"
category: "reference"
tags: [reference, langgraph-sdk, schema, taskresultpayload]
---

# TaskResultPayload

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/TaskResultPayload)

Payload for a task result event.

## Signature

```python
TaskResultPayload()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    id: str,
    name: str,
    error: str | None,
    interrupts: list[dict[str, Any]],
    result: dict[str, Any],
)
```

| Name | Type |
|------|------|
| `id` | `str` |
| `name` | `str` |
| `error` | `str \| None` |
| `interrupts` | `list[dict[str, Any]]` |
| `result` | `dict[str, Any]` |

## Properties

- `id`
- `name`
- `error`
- `interrupts`
- `result`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/sdk-py/langgraph_sdk/schema.py#L632)
