---
title: "StoreGet"
description: "Operation to retrieve a specific item by its namespace and key."
source: "https://reference.langchain.com/python/langgraph-sdk/auth/types/StoreGet"
category: "reference"
tags: [reference, langgraph-sdk, auth, types, storeget]
---

# StoreGet

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/auth/types/StoreGet)

Operation to retrieve a specific item by its namespace and key.

This dict is mutable — auth handlers can modify `namespace` to enforce
access scoping (e.g., prepending the user's identity).

## Signature

```python
StoreGet()
```

## Extends

- `typing.TypedDict`

## Constructors

```python
__init__(
    namespace: tuple[str, ...],
    key: str,
)
```

| Name | Type |
|------|------|
| `namespace` | `tuple[str, ...]` |
| `key` | `str` |

## Properties

- `namespace`
- `key`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5db97b9ccab6b8d9a5ab1e8f0bebea7c03a8708a/libs/sdk-py/langgraph_sdk/auth/types.py#L862)
