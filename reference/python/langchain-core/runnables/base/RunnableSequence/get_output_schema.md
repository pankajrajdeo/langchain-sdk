---
title: "get_output_schema"
description: "Get the output schema of the Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableSequence/get_output_schema"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnablesequence, get_output_schema]
---

# get_output_schema

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableSequence/get_output_schema)

Get the output schema of the `Runnable`.

## Signature

```python
get_output_schema(
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

The output schema of the `Runnable`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d4dafe5839c4a6b07d71cc78697df0de9e627e21/libs/core/langchain_core/runnables/base.py#L3283)
