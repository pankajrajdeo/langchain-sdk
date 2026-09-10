---
title: "RunLog"
description: "Run log."
source: "https://reference.langchain.com/python/langchain-core/tracers/log_stream/RunLog"
category: "reference"
tags: [reference, langchain-core, tracers, log_stream, runlog]
---

# RunLog

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/log_stream/RunLog)

Run log.

## Signature

```python
RunLog(
    self,
    *ops: dict[str, Any] = (),
    state: RunState,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `*ops` | `dict[str, Any]` | No | The operations to apply to the state. (default: `()`) |
| `state` | `RunState` | Yes | The initial state of the run log. |

## Extends

- `RunLogPatch`

## Constructors

```python
__init__(
    self,
    *ops: dict[str, Any] = (),
    state: RunState,
) -> None
```

| Name | Type |
|------|------|
| `state` | `RunState` |

## Properties

- `state`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/tracers/log_stream.py#L168)
