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
    kwargs: Any | None = {},
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/b4aa7e7d00c452251720ce30b8bc2c41ca44e1f5/libs/core/langchain_core/runnables/base.py#L5335)
