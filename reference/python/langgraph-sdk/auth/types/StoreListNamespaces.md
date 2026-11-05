---
title: "StoreListNamespaces"
description: "Operation to list and filter namespaces in the store."
source: "https://reference.langchain.com/python/langgraph-sdk/auth/types/StoreListNamespaces"
category: "reference"
tags: [reference, langgraph-sdk, auth, types, storelistnamespaces]
---

# StoreListNamespaces

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/auth/types/StoreListNamespaces)

Operation to list and filter namespaces in the store.

This dict is mutable — auth handlers can modify `namespace` (the prefix)
to enforce access scoping (e.g., prepending the user's identity).

## Signature

```python
StoreListNamespaces()
```

## Extends

- `typing.TypedDict`

## Constructors

```python
__init__(
    namespace: tuple[str, ...] | None,
    suffix: tuple[str, ...] | None,
    max_depth: int | None,
    limit: int,
    offset: int,
)
```

| Name | Type |
|------|------|
| `namespace` | `tuple[str, ...] \| None` |
| `suffix` | `tuple[str, ...] \| None` |
| `max_depth` | `int \| None` |
| `limit` | `int` |
| `offset` | `int` |

## Properties

- `namespace`
- `suffix`
- `max_depth`
- `limit`
- `offset`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/sdk-py/langgraph_sdk/auth/types.py#L905)
