---
title: "CronsUpdate"
description: "Payload for updating a cron job."
source: "https://reference.langchain.com/python/langgraph-sdk/auth/types/CronsUpdate"
category: "reference"
tags: [reference, langgraph-sdk, auth, types, cronsupdate]
---

# CronsUpdate

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/auth/types/CronsUpdate)

Payload for updating a cron job.

???+ example "Examples"

```python
    update_params = {
        "cron_id": UUID("123e4567-e89b-12d3-a456-426614174000"),
        "payload": {"key": "value"},
        "schedule": "0 0 * * *"
    }
```

## Signature

```python
CronsUpdate()
```

## Extends

- `typing.TypedDict`

## Constructors

```python
__init__(
    cron_id: UUID,
    payload: dict[str, typing.Any] | None,
    schedule: str | None,
)
```

| Name | Type |
|------|------|
| `cron_id` | `UUID` |
| `payload` | `dict[str, typing.Any] \| None` |
| `schedule` | `str \| None` |

## Properties

- `cron_id`
- `payload`
- `schedule`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/sdk-py/langgraph_sdk/auth/types.py#L810)
