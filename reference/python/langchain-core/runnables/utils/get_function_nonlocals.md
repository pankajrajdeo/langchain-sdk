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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/runnables/utils.py#L411)
