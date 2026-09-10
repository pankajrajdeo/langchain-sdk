---
title: "AsyncCallbackManagerForChainGroup"
description: "Async callback manager for the chain group."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForChainGroup"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, asynccallbackmanagerforchaingroup]
---

# AsyncCallbackManagerForChainGroup

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForChainGroup)

Async callback manager for the chain group.

## Signature

```python
AsyncCallbackManagerForChainGroup(
    self,
    handlers: list[BaseCallbackHandler],
    inheritable_handlers: list[BaseCallbackHandler] | None = None,
    parent_run_id: UUID | None = None,
    *,
    parent_run_manager: AsyncCallbackManagerForChainRun,
    **kwargs: Any = {},
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `handlers` | `list[BaseCallbackHandler]` | Yes | The list of handlers. |
| `inheritable_handlers` | `list[BaseCallbackHandler] \| None` | No | The list of inheritable handlers. (default: `None`) |
| `parent_run_id` | `UUID \| None` | No | The ID of the parent run. (default: `None`) |
| `parent_run_manager` | `AsyncCallbackManagerForChainRun` | Yes | The parent run manager. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

## Extends

- `AsyncCallbackManager`

## Constructors

```python
__init__(
    self,
    handlers: list[BaseCallbackHandler],
    inheritable_handlers: list[BaseCallbackHandler] | None = None,
    parent_run_id: UUID | None = None,
    *,
    parent_run_manager: AsyncCallbackManagerForChainRun,
    **kwargs: Any = {},
) -> None
```

| Name | Type |
|------|------|
| `handlers` | `list[BaseCallbackHandler]` |
| `inheritable_handlers` | `list[BaseCallbackHandler] \| None` |
| `parent_run_id` | `UUID \| None` |
| `parent_run_manager` | `AsyncCallbackManagerForChainRun` |

## Properties

- `parent_run_manager`
- `ended`

## Methods

- [`copy()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForChainGroup/copy)
- [`merge()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForChainGroup/merge)
- [`on_chain_end()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForChainGroup/on_chain_end)
- [`on_chain_error()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForChainGroup/on_chain_error)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/callbacks/manager.py#L2257)
