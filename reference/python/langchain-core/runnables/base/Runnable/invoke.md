---
title: "invoke"
description: "Transform a single input into an output."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/invoke"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnable, invoke]
---

# invoke

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/invoke)

Transform a single input into an output.

## Signature

```python
invoke(
    self,
    input: Input,
    config: RunnableConfig | None = None,
    **kwargs: Any = {},
) -> Output
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input` | `Input` | Yes | The input to the `Runnable`. |
| `config` | `RunnableConfig \| None` | No | A config to use when invoking the `Runnable`.  The config supports standard keys like `'tags'`, `'metadata'` for tracing purposes, `'max_concurrency'` for controlling how much work to do in parallel, and other keys.  Please refer to `RunnableConfig` for more details. (default: `None`) |

## Returns

`Output`

The output of the `Runnable`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/runnables/base.py#L885)
