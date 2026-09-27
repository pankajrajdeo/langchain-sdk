---
title: "config_schema"
description: "The type of config this Runnable accepts specified as a Pydantic model."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/config_schema"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnable, config_schema]
---

# config_schema

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/config_schema)

The type of config this `Runnable` accepts specified as a Pydantic model.

To mark a field as configurable, see the `configurable_fields`
and `configurable_alternatives` methods.

## Signature

```python
config_schema(
    self,
    *,
    include: Sequence[str] | None = None,
) -> type[BaseModel]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `include` | `Sequence[str] \| None` | No | A list of fields to include in the config schema. (default: `None`) |

## Returns

`type[BaseModel]`

A Pydantic model that can be used to validate config.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/runnables/base.py#L534)
