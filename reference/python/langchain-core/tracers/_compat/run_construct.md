---
title: "run_construct"
description: "Construct run without validation, compatible with both Pydantic v1 and v2."
source: "https://reference.langchain.com/python/langchain-core/tracers/_compat/run_construct"
category: "reference"
tags: [reference, langchain-core, tracers, compat, run_construct]
---

# run_construct

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/_compat/run_construct)

Construct run without validation, compatible with both Pydantic v1 and v2.

## Signature

```python
run_construct(
    **kwargs: Any = {},
) -> Run
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `**kwargs` | `Any` | No | Fields to set on the run. (default: `{}`) |

## Returns

`Run`

A new `Run` instance constructed without validation.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/tracers/_compat.py#L54)
