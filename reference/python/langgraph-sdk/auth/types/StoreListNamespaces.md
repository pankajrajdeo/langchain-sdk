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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5db97b9ccab6b8d9a5ab1e8f0bebea7c03a8708a/libs/sdk-py/langgraph_sdk/auth/types.py#L905)
