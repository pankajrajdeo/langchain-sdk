---
title: "shielded"
description: "Makes so an awaitable method is always shielded from cancellation."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/shielded"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, shielded]
---

# shielded

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/shielded)

Makes so an awaitable method is always shielded from cancellation.

## Signature

```python
shielded(
    func: Func,
) -> Func
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `func` | `Func` | Yes | The function to shield. |

## Returns

`Func`

The shielded function

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/bdf0f53ed0aec3c9ae371a549e1a4d2ee4e9f021/libs/core/langchain_core/callbacks/manager.py#L232)
