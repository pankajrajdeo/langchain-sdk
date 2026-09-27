---
title: "on_chain_end"
description: "Run when traced chain group ends."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForChainGroup/on_chain_end"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, asynccallbackmanagerforchaingroup, on_chain_end]
---

# on_chain_end

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForChainGroup/on_chain_end)

Run when traced chain group ends.

## Signature

```python
on_chain_end(
    self,
    outputs: dict[str, Any] | Any,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `outputs` | `dict[str, Any] \| Any` | Yes | The outputs of the chain. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/callbacks/manager.py#L2362)
