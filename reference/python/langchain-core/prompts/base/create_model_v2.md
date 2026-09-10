---
title: "create_model_v2"
description: "Create a Pydantic model with the given field definitions."
source: "https://reference.langchain.com/python/langchain-core/prompts/base/create_model_v2"
category: "reference"
tags: [reference, langchain-core, prompts, base, create_model_v2]
---

# create_model_v2

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/pydantic/create_model_v2)

Create a Pydantic model with the given field definitions.

!!! warning

    Do not use outside of langchain packages. This API is subject to change at any
    time.

## Signature

```python
create_model_v2(
    model_name: str,
    *,
    module_name: str | None = None,
    field_definitions: dict[str, Any] | None = None,
    root: Any | None = None,
) -> type[BaseModel]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `model_name` | `str` | Yes | The name of the model. |
| `module_name` | `str \| None` | No | The name of the module where the model is defined.  This is used by Pydantic to resolve any forward references. (default: `None`) |
| `field_definitions` | `dict[str, Any] \| None` | No | The field definitions for the model. (default: `None`) |
| `root` | `Any \| None` | No | Type for a root model (`RootModel`) (default: `None`) |

## Returns

`type[BaseModel]`

The created model.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/utils/pydantic.py#L557)
