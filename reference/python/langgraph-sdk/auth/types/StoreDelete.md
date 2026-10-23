---
title: "StoreDelete"
description: "Operation to delete an item from the store."
source: "https://reference.langchain.com/python/langgraph-sdk/auth/types/StoreDelete"
category: "reference"
tags: [reference, langgraph-sdk, auth, types, storedelete]
---

# StoreDelete

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/auth/types/StoreDelete)

Operation to delete an item from the store.

This dict is mutable — auth handlers can modify `namespace` to enforce
access scoping (e.g., prepending the user's identity).

## Signature

```python
StoreDelete()
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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/sdk-py/langgraph_sdk/auth/types.py#L959)
