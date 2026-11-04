---
title: "TaskPayload"
description: "Payload for a task start event."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/TaskPayload"
category: "reference"
tags: [reference, langgraph-sdk, schema, taskpayload]
---

# TaskPayload

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/TaskPayload)

Payload for a task start event.

## Signature

```python
TaskPayload()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    id: str,
    name: str,
    input: Any,
    triggers: list[str],
)
```

| Name | Type |
|------|------|
| `id` | `str` |
| `name` | `str` |
| `input` | `Any` |
| `triggers` | `list[str]` |

## Properties

- `id`
- `name`
- `input`
- `triggers`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5db97b9ccab6b8d9a5ab1e8f0bebea7c03a8708a/libs/sdk-py/langgraph_sdk/schema.py#L619)
