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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/04ac76c07ec173a44e3e57de54861d0b637e3299/libs/core/langchain_core/callbacks/manager.py#L221)
