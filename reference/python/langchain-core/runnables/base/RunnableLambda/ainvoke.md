---
title: "ainvoke"
description: "Invoke this Runnable asynchronously."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableLambda/ainvoke"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnablelambda, ainvoke]
---

# ainvoke

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableLambda/ainvoke)

Invoke this `Runnable` asynchronously.

## Signature

```python
ainvoke(
    self,
    input: Input,
    config: RunnableConfig | None = None,
    **kwargs: Any | None = {},
) -> Output
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input` | `Input` | Yes | The input to this `Runnable`. |
| `config` | `RunnableConfig \| None` | No | The config to use. (default: `None`) |
| `**kwargs` | `Any \| None` | No | Additional keyword arguments. (default: `{}`) |

## Returns

`Output`

The output of this `Runnable`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/base.py#L5332)
