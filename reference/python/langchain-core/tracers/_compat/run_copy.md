---
title: "run_copy"
description: "Copy run, compatible with both Pydantic v1 and v2."
source: "https://reference.langchain.com/python/langchain-core/tracers/_compat/run_copy"
category: "reference"
tags: [reference, langchain-core, tracers, compat, run_copy]
---

# run_copy

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/_compat/run_copy)

Copy run, compatible with both Pydantic v1 and v2.

## Signature

```python
run_copy(
    run: Run,
    **kwargs: Any = {},
) -> Run
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `run` | `Run` | Yes | The run to copy. |
| `**kwargs` | `Any` | No | Additional arguments passed to `model_copy`/`copy`. (default: `{}`) |

## Returns

`Run`

A copy of the run.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/tracers/_compat.py#L39)
