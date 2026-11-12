---
title: "get_fields"
description: "Return the field names of a Pydantic model."
source: "https://reference.langchain.com/python/langchain-core/tools/base/get_fields"
category: "reference"
tags: [reference, langchain-core, tools, base, get_fields]
---

# get_fields

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/pydantic/get_fields)

Return the field names of a Pydantic model.

## Signature

```python
get_fields(
    model: type[BaseModel | BaseModelV1] | BaseModel | BaseModelV1,
) -> dict[str, FieldInfoV2] | dict[str, ModelField]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `model` | `type[BaseModel \| BaseModelV1] \| BaseModel \| BaseModelV1` | Yes | The Pydantic model or instance. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/utils/pydantic.py#L330)
