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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ea17e48f0a4336c920394fd029de99f1568b4c38/libs/core/langchain_core/runnables/base.py#L4078)
