---
title: "AssistantsRead"
description: "Payload for reading an assistant."
source: "https://reference.langchain.com/python/langgraph-sdk/auth/types/AssistantsRead"
category: "reference"
tags: [reference, langgraph-sdk, auth, types, assistantsread]
---

# AssistantsRead

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/auth/types/AssistantsRead)

Payload for reading an assistant.

???+ example "Examples"

```python
    read_params = {
        "assistant_id": UUID("123e4567-e89b-12d3-a456-426614174000"),
        "metadata": {"owner": "user123"}
    }
```

## Signature

```python
AssistantsRead()
```

## Extends

- `typing.TypedDict`

## Constructors

```python
__init__(
    assistant_id: UUID,
    metadata: MetadataInput,
)
```

| Name | Type |
|------|------|
| `assistant_id` | `UUID` |
| `metadata` | `MetadataInput` |

## Properties

- `assistant_id`
- `metadata`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/sdk-py/langgraph_sdk/auth/types.py#L638)
