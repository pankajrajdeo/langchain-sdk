---
title: "MinimalUserDict"
description: "The dictionary representation of a user."
source: "https://reference.langchain.com/python/langgraph-sdk/auth/types/MinimalUserDict"
category: "reference"
tags: [reference, langgraph-sdk, auth, types, minimaluserdict]
---

# MinimalUserDict

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/auth/types/MinimalUserDict)

The dictionary representation of a user.

## Signature

```python
MinimalUserDict()
```

## Extends

- `typing.TypedDict`

## Constructors

```python
__init__(
    identity: typing_extensions.Required[str],
    display_name: str,
    is_authenticated: bool,
    permissions: Sequence[str],
)
```

| Name | Type |
|------|------|
| `identity` | `typing_extensions.Required[str]` |
| `display_name` | `str` |
| `is_authenticated` | `bool` |
| `permissions` | `Sequence[str]` |

## Properties

- `identity`
- `display_name`
- `is_authenticated`
- `permissions`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/6b83b9b019c9b2680e4456dd6835d0fea27b9887/libs/sdk-py/langgraph_sdk/auth/types.py#L164)
