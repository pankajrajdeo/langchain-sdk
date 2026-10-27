---
title: "CronsDelete"
description: "Payload for deleting a cron job."
source: "https://reference.langchain.com/python/langgraph-sdk/auth/types/CronsDelete"
category: "reference"
tags: [reference, langgraph-sdk, auth, types, cronsdelete]
---

# CronsDelete

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/auth/types/CronsDelete)

Payload for deleting a cron job.

???+ example "Examples"

```python
    delete_params = {
        "cron_id": UUID("123e4567-e89b-12d3-a456-426614174000")
    }
```

## Signature

```python
CronsDelete()
```

## Extends

- `typing.TypedDict`

## Constructors

```python
__init__(
    cron_id: UUID,
)
```

| Name | Type |
|------|------|
| `cron_id` | `UUID` |

## Properties

- `cron_id`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/sdk-py/langgraph_sdk/auth/types.py#L778)
