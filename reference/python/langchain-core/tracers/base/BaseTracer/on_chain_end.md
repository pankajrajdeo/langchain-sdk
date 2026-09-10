---
title: "on_chain_end"
description: "End a trace for a chain run."
source: "https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_chain_end"
category: "reference"
tags: [reference, langchain-core, tracers, base, basetracer, on_chain_end]
---

# on_chain_end

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_chain_end)

End a trace for a chain run.

## Signature

```python
on_chain_end(
    self,
    outputs: dict[str, Any],
    *,
    run_id: UUID,
    inputs: dict[str, Any] | None = None,
    **kwargs: Any = {},
) -> Run
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `outputs` | `dict[str, Any]` | Yes | The outputs for the chain. |
| `run_id` | `UUID` | Yes | The run ID. |
| `inputs` | `dict[str, Any] \| None` | No | The inputs for the chain. (default: `None`) |
| `**kwargs` | `Any` | No | Additional arguments. (default: `{}`) |

## Returns

`Run`

The run.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/tracers/base.py#L305)
