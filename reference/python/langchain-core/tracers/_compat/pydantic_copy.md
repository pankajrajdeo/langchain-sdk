---
title: "pydantic_copy"
description: "Copy any Pydantic model, compatible with both v1 and v2."
source: "https://reference.langchain.com/python/langchain-core/tracers/_compat/pydantic_copy"
category: "reference"
tags: [reference, langchain-core, tracers, compat, pydantic_copy]
---

# pydantic_copy

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/_compat/pydantic_copy)

Copy any Pydantic model, compatible with both v1 and v2.

## Signature

```python
pydantic_copy(
    obj: T,
    **kwargs: Any = {},
) -> T
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `obj` | `T` | Yes | The Pydantic model to copy. |
| `**kwargs` | `Any` | No | Additional arguments passed to `model_copy`/`copy`. (default: `{}`) |

## Returns

`T`

A copy of the model.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/tracers/_compat.py#L83)
