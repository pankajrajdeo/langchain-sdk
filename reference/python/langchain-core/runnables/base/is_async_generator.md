---
title: "is_async_generator"
description: "Check if a function is an async generator."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/is_async_generator"
category: "reference"
tags: [reference, langchain-core, runnables, base, is_async_generator]
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/runnables/utils.py#L768)
