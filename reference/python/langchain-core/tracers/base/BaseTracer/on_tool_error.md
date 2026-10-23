---
title: "on_tool_error"
description: "Handle an error for a tool run."
source: "https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_tool_error"
category: "reference"
tags: [reference, langchain-core, tracers, base, basetracer, on_tool_error]
---

# on_tool_error

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_tool_error)

Handle an error for a tool run.

## Signature

```python
on_tool_error(
    self,
    error: BaseException,
    *,
    run_id: UUID,
    kwargs: Any = {},
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/tracers/base.py#L427)
