---
title: "stream"
description: "Default implementation of stream, which calls invoke."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/stream"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnable, stream]
---

# stream

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/stream)

Default implementation of `stream`, which calls `invoke`.

Subclasses must override this method if they support streaming output.

## Signature

```python
stream(
    self,
    input: Input,
    config: RunnableConfig | None = None,
    **kwargs: Any | None = {},
) -> Iterator[Output]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input` | `Input` | Yes | The input to the `Runnable`. |
| `config` | `RunnableConfig \| None` | No | The config to use for the `Runnable`. (default: `None`) |
| `**kwargs` | `Any \| None` | No | Additional keyword arguments to pass to the `Runnable`. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/base.py#L1194)
