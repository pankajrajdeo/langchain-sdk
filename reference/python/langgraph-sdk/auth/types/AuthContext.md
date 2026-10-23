---
title: "AuthContext"
description: "Complete authentication context with resource and action information."
source: "https://reference.langchain.com/python/langgraph-sdk/auth/types/AuthContext"
category: "reference"
tags: [reference, langgraph-sdk, auth, types, authcontext]
---

# AuthContext

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/auth/types/AuthContext)

Complete authentication context with resource and action information.

Extends BaseAuthContext with specific resource and action being accessed,
allowing for fine-grained access control decisions.

## Signature

```python
AuthContext(
    self,
    permissions: Sequence[str],
    user: BaseUser,
    resource: typing.Literal['runs', 'threads', 'crons', 'assistants', 'store'],
    action: typing.Literal['create', 'read', 'update', 'delete', 'search', 'create_run', 'put', 'get', 'list_namespaces'],
)
```

## Extends

- `BaseAuthContext`

## Constructors

```python
__init__(
    self,
    permissions: Sequence[str],
    user: BaseUser,
    resource: typing.Literal['runs', 'threads', 'crons', 'assistants', 'store'],
    action: typing.Literal['create', 'read', 'update', 'delete', 'search', 'create_run', 'put', 'get', 'list_namespaces'],
) -> None
```

| Name | Type |
|------|------|
| `permissions` | `Sequence[str]` |
| `user` | `BaseUser` |
| `resource` | `typing.Literal['runs', 'threads', 'crons', 'assistants', 'store']` |
| `action` | `typing.Literal['create', 'read', 'update', 'delete', 'search', 'create_run', 'put', 'get', 'list_namespaces']` |

## Properties

- `resource`
- `action`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/sdk-py/langgraph_sdk/auth/types.py#L388)
