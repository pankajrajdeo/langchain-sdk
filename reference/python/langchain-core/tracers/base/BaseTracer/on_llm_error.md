---
title: "on_llm_error"
description: "Handle an error for an LLM run."
source: "https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_llm_error"
category: "reference"
tags: [reference, langchain-core, tracers, base, basetracer, on_llm_error]
---

# on_llm_error

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_llm_error)

Handle an error for an LLM run.

## Signature

```python
on_llm_error(
    self,
    error: BaseException,
    *,
    run_id: UUID,
    **kwargs: Any = {},
) -> Run
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `error` | `BaseException` | Yes | The error. |
| `run_id` | `UUID` | Yes | The run ID. |
| `**kwargs` | `Any` | No | Additional arguments. (default: `{}`) |

## Returns

`Run`

The run.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/tracers/base.py#L234)
