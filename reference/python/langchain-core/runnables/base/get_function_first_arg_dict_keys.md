---
title: "get_function_first_arg_dict_keys"
description: "Get the keys of the first argument of a function if it is a dict."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/get_function_first_arg_dict_keys"
category: "reference"
tags: [reference, langchain-core, runnables, base, get_function_first_arg_dict_keys]
---

# get_function_first_arg_dict_keys

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/get_function_first_arg_dict_keys)

Get the keys of the first argument of a function if it is a dict.

## Signature

```python
get_function_first_arg_dict_keys(
    func: Callable[..., Any],
) -> list[str] | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `func` | `Callable[..., Any]` | Yes | The function to check. |

## Returns

`list[str] | None`

The keys of the first argument if it is a dict, None otherwise.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/utils.py#L368)
