---
title: "Item"
description: "Represents a single document or data entry in the graph's Store."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/Item"
category: "reference"
tags: [reference, langgraph-sdk, schema, item]
---

# Item

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/Item)

Represents a single document or data entry in the graph's Store.

Items are used to store cross-thread memories.

## Signature

```python
Item()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    namespace: list[str],
    key: str,
    value: dict[str, Any],
    created_at: datetime,
    updated_at: datetime,
)
```

| Name | Type |
|------|------|
| `namespace` | `list[str]` |
| `key` | `str` |
| `value` | `dict[str, Any]` |
| `created_at` | `datetime` |
| `updated_at` | `datetime` |

## Properties

- `namespace`
- `key`
- `value`
- `created_at`
- `updated_at`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/sdk-py/langgraph_sdk/schema.py#L551)
