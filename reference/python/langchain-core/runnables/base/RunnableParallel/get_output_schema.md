---
title: "get_output_schema"
description: "Get the output schema of the Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableParallel/get_output_schema"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnableparallel, get_output_schema]
---

# get_output_schema

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableParallel/get_output_schema)

Get the output schema of the `Runnable`.

## Signature

```python
get_output_schema(
    self,
    config: RunnableConfig | None = None,
) -> type[BaseModel]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig \| None` | No | The config to use. (default: `None`) |

## Returns

`type[BaseModel]`

The output schema of the `Runnable`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/runnables/base.py#L4063)
