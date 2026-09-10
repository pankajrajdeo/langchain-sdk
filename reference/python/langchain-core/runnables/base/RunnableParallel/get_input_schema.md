---
title: "get_input_schema"
description: "Get the input schema of the Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableParallel/get_input_schema"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnableparallel, get_input_schema]
---

# get_input_schema

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableParallel/get_input_schema)

Get the input schema of the `Runnable`.

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

The input schema of the `Runnable`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/base.py#L4021)
