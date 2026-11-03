---
title: "is_async_generator"
description: "Check if a function is an async generator."
source: "https://reference.langchain.com/python/langchain-core/runnables/utils/is_async_generator"
category: "reference"
tags: [reference, langchain-core, runnables, utils, is_async_generator]
---

# is_async_generator

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/is_async_generator)

Check if a function is an async generator.

## Signature

```python
is_async_generator(
    func: Any,
) -> TypeGuard[Callable[..., AsyncIterator[Any]]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `func` | `Any` | Yes | The function to check. |

## Returns

`TypeGuard[Callable[..., AsyncIterator[Any]]]`

`True` if the function is an async generator, `False` otherwise.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/e936943647fe9bd9c4c24122ee3e1812ead82130/libs/core/langchain_core/runnables/utils.py#L768)
