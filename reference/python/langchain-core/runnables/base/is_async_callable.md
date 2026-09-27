---
title: "is_async_callable"
description: "Check if a function is async."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/is_async_callable"
category: "reference"
tags: [reference, langchain-core, runnables, base, is_async_callable]
---

# is_async_callable

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/is_async_callable)

Check if a function is async.

## Signature

```python
is_async_callable(
    func: Any,
) -> TypeGuard[Callable[..., Awaitable[Any]]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `func` | `Any` | Yes | The function to check. |

## Returns

`TypeGuard[Callable[..., Awaitable[Any]]]`

`True` if the function is async, `False` otherwise.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/runnables/utils.py#L784)
