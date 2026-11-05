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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/sdk-py/langgraph_sdk/auth/types.py#L698)
