---
title: "on_retry"
description: "Run on retry."
source: "https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_retry"
category: "reference"
tags: [reference, langchain-core, tracers, base, basetracer, on_retry]
---

# on_retry

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_retry)

Run on retry.

## Signature

```python
on_retry(
    self,
    retry_state: RetryCallState,
    *,
    run_id: UUID,
    **kwargs: Any = {},
) -> Run
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `retry_state` | `RetryCallState` | Yes | The retry state. |
| `run_id` | `UUID` | Yes | The run ID. |
| `**kwargs` | `Any` | No | Additional arguments. (default: `{}`) |

## Returns

`Run`

The run.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/tracers/base.py#L184)
