---
title: "get_input_schema"
description: "The Pydantic schema for the input to this Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableLambda/get_input_schema"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnablelambda, get_input_schema]
---

# get_input_schema

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableLambda/get_input_schema)

The Pydantic schema for the input to this `Runnable`.

## Signature

```python
get_input_schema(
    self,
    config: RunnableConfig | None = None,
) -> TypeBaseModel
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig \| None` | No | The config to use. (default: `None`) |

## Returns

`TypeBaseModel`

The input schema for this `Runnable`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/runnables/base.py#L4973)
