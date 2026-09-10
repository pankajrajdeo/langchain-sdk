---
title: "transform"
description: "Transform inputs to outputs."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/transform"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnable, transform]
---

# transform

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/transform)

Transform inputs to outputs.

Default implementation of transform, which buffers input and calls `astream`.

Subclasses must override this method if they can start producing output while
input is still being generated.

## Signature

```python
transform(
    self,
    input: Iterator[Input],
    config: RunnableConfig | None = None,
    **kwargs: Any | None = {},
) -> Iterator[Output]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input` | `Iterator[Input]` | Yes | An iterator of inputs to the `Runnable`. |
| `config` | `RunnableConfig \| None` | No | The config to use for the `Runnable`. (default: `None`) |
| `**kwargs` | `Any \| None` | No | Additional keyword arguments to pass to the `Runnable`. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/base.py#L1760)
