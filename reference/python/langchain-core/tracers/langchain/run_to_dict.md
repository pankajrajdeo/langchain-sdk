---
title: "run_to_dict"
description: "Convert run to dict, compatible with both Pydantic v1 and v2."
source: "https://reference.langchain.com/python/langchain-core/tracers/langchain/run_to_dict"
category: "reference"
tags: [reference, langchain-core, tracers, langchain, run_to_dict]
---

# run_to_dict

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/_compat/run_to_dict)

Convert run to dict, compatible with both Pydantic v1 and v2.

## Signature

```python
run_to_dict(
    run: Run,
    **kwargs: Any = {},
) -> dict[str, Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `run` | `Run` | Yes | The run to convert. |
| `**kwargs` | `Any` | No | Additional arguments passed to `model_dump`/`dict`. (default: `{}`) |

## Returns

`dict[str, Any]`

Dictionary representation of the run.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/tracers/_compat.py#L24)
