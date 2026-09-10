---
title: "pydantic_to_dict"
description: "Convert any Pydantic model to dict, compatible with both v1 and v2."
source: "https://reference.langchain.com/python/langchain-core/tracers/_compat/pydantic_to_dict"
category: "reference"
tags: [reference, langchain-core, tracers, compat, pydantic_to_dict]
---

# pydantic_to_dict

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/_compat/pydantic_to_dict)

Convert any Pydantic model to dict, compatible with both v1 and v2.

## Signature

```python
pydantic_to_dict(
    obj: Any,
    **kwargs: Any = {},
) -> dict[str, Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `obj` | `Any` | Yes | The Pydantic model to convert. |
| `**kwargs` | `Any` | No | Additional arguments passed to `model_dump`/`dict`. (default: `{}`) |

## Returns

`dict[str, Any]`

Dictionary representation of the model.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/tracers/_compat.py#L68)
