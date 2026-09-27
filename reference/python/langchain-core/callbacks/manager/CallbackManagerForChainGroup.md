---
title: "CallbackManagerForChainGroup"
description: "Callback manager for the chain group."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForChainGroup"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, callbackmanagerforchaingroup]
---

# CallbackManagerForChainGroup

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForChainGroup)

Callback manager for the chain group.

## Signature

```python
CallbackManagerForChainGroup(
    self,
    handlers: list[BaseCallbackHandler],
    inheritable_handlers: list[BaseCallbackHandler] | None = None,
    parent_run_id: UUID | None = None,
    *,
    parent_run_manager: CallbackManagerForChainRun,
    **kwargs: Any = {},
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `handlers` | `list[BaseCallbackHandler]` | Yes | The list of handlers. |
| `inheritable_handlers` | `list[BaseCallbackHandler] \| None` | No | The list of inheritable handlers. (default: `None`) |
| `parent_run_id` | `UUID \| None` | No | The ID of the parent run. (default: `None`) |
| `parent_run_manager` | `CallbackManagerForChainRun` | Yes | The parent run manager. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

## Extends

- `CallbackManager`

## Constructors

```python
__init__(
    self,
    handlers: list[BaseCallbackHandler],
    inheritable_handlers: list[BaseCallbackHandler] | None = None,
    parent_run_id: UUID | None = None,
    *,
    parent_run_manager: CallbackManagerForChainRun,
    **kwargs: Any = {},
) -> None
```

| Name | Type |
|------|------|
| `handlers` | `list[BaseCallbackHandler]` |
| `inheritable_handlers` | `list[BaseCallbackHandler] \| None` |
| `parent_run_id` | `UUID \| None` |
| `parent_run_manager` | `CallbackManagerForChainRun` |

## Properties

- `parent_run_manager`
- `ended`

## Methods

- [`copy()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForChainGroup/copy)
- [`merge()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForChainGroup/merge)
- [`on_chain_end()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForChainGroup/on_chain_end)
- [`on_chain_error()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForChainGroup/on_chain_error)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/callbacks/manager.py#L1728)
