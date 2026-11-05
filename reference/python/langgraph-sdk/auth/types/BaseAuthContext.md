---
title: "BaseAuthContext"
description: "Base class for authentication context."
source: "https://reference.langchain.com/python/langgraph-sdk/auth/types/BaseAuthContext"
category: "reference"
tags: [reference, langgraph-sdk, auth, types, baseauthcontext]
---

# BaseAuthContext

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/auth/types/BaseAuthContext)

Base class for authentication context.

Provides the fundamental authentication information needed for
authorization decisions.

## Signature

```python
BaseAuthContext(
    self,
    permissions: Sequence[str],
    user: BaseUser,
)
```

## Constructors

```python
__init__(
    self,
    permissions: Sequence[str],
    user: BaseUser,
) -> None
```

| Name | Type |
|------|------|
| `permissions` | `Sequence[str]` |
| `user` | `BaseUser` |

## Properties

- `permissions`
- `user`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/sdk-py/langgraph_sdk/auth/types.py#L373)
