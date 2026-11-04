---
title: "AssistantsDelete"
description: "Payload for deleting an assistant."
source: "https://reference.langchain.com/python/langgraph-sdk/auth/types/AssistantsDelete"
category: "reference"
tags: [reference, langgraph-sdk, auth, types, assistantsdelete]
---

# AssistantsDelete

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/auth/types/AssistantsDelete)

Payload for deleting an assistant.

???+ example "Examples"

```python
    delete_params = {
        "assistant_id": UUID("123e4567-e89b-12d3-a456-426614174000")
    }
```

## Signature

```python
AssistantsDelete()
```

## Extends

- `typing.TypedDict`

## Constructors

```python
__init__(
    assistant_id: UUID,
)
```

| Name | Type |
|------|------|
| `assistant_id` | `UUID` |

## Properties

- `assistant_id`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5db97b9ccab6b8d9a5ab1e8f0bebea7c03a8708a/libs/sdk-py/langgraph_sdk/auth/types.py#L698)
