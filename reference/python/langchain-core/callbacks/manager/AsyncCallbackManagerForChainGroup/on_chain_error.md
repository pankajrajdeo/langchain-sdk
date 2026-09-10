---
title: "on_chain_error"
description: "Run when chain errors."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForChainGroup/on_chain_error"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, asynccallbackmanagerforchaingroup, on_chain_error]
---

# on_chain_error

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForChainGroup/on_chain_error)

Run when chain errors.

## Signature

```python
on_chain_error(
    self,
    error: BaseException,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `error` | `BaseException` | Yes | The error. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/callbacks/manager.py#L2372)
