---
title: "with_types"
description: "Bind input and output types to a Runnable, returning a new Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/with_types"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnable, with_types]
---

# with_types

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/with_types)

Bind input and output types to a `Runnable`, returning a new `Runnable`.

## Signature

```python
with_types(
    self,
    *,
    input_type: type[Input] | None = None,
    output_type: type[Output] | None = None,
) -> Runnable[Input, Output]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input_type` | `type[Input] \| None` | No | The input type to bind to the `Runnable`. (default: `None`) |
| `output_type` | `type[Output] \| None` | No | The output type to bind to the `Runnable`. (default: `None`) |

## Returns

`Runnable[Input, Output]`

A new `Runnable` with the types bound.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/runnables/base.py#L2079)
