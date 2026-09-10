---
title: "RunCollectorCallbackHandler"
description: "Tracer that collects all nested runs in a list."
source: "https://reference.langchain.com/python/langchain-core/tracers/run_collector/RunCollectorCallbackHandler"
category: "reference"
tags: [reference, langchain-core, tracers, run_collector, runcollectorcallbackhandler]
---

# RunCollectorCallbackHandler

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/run_collector/RunCollectorCallbackHandler)

Tracer that collects all nested runs in a list.

This tracer is useful for inspection and evaluation purposes.

## Signature

```python
RunCollectorCallbackHandler(
    self,
    example_id: UUID | str | None = None,
    **kwargs: Any = {},
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `example_id` | `UUID \| str \| None` | No | The ID of the example being traced. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

## Extends

- `BaseTracer`

## Constructors

```python
__init__(
    self,
    example_id: UUID | str | None = None,
    **kwargs: Any = {},
) -> None
```

| Name | Type |
|------|------|
| `example_id` | `UUID \| str \| None` |

## Properties

- `name`
- `example_id`
- `traced_runs`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/tracers/run_collector.py#L11)
