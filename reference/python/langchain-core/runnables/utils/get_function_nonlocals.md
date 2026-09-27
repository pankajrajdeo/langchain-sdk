---
title: "get_function_nonlocals"
description: "Get the nonlocal variables accessed by a function."
source: "https://reference.langchain.com/python/langchain-core/runnables/utils/get_function_nonlocals"
category: "reference"
tags: [reference, langchain-core, runnables, utils, get_function_nonlocals]
---

# get_function_nonlocals

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/get_function_nonlocals)

Get the nonlocal variables accessed by a function.

## Signature

```python
get_function_nonlocals(
    func: Callable[..., Any],
) -> list[Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `func` | `Callable[..., Any]` | Yes | The function to check. |

## Returns

`list[Any]`

The nonlocal variables accessed by the function.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/runnables/utils.py#L410)
