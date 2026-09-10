---
title: "prepare"
description: "Prepare the Runnable for invocation."
source: "https://reference.langchain.com/python/langchain-core/runnables/configurable/DynamicRunnable/prepare"
category: "reference"
tags: [reference, langchain-core, runnables, configurable, dynamicrunnable, prepare]
---

# prepare

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/configurable/DynamicRunnable/prepare)

Prepare the `Runnable` for invocation.

## Signature

```python
prepare(
    self,
    config: RunnableConfig | None = None,
) -> tuple[Runnable[Input, Output], RunnableConfig]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig \| None` | No | The configuration to use. (default: `None`) |

## Returns

`tuple[Runnable[Input, Output], RunnableConfig]`

The prepared `Runnable` and configuration.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/configurable.py#L119)
