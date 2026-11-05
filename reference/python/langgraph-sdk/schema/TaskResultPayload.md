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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/sdk-py/langgraph_sdk/schema.py#L650)
