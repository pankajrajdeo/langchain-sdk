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
    ops: dict[str, Any] = (),
    *,
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
    ops: dict[str, Any] = (),
    *,
    state: RunState,
) -> None
```

| Name | Type |
|------|------|
| `ops` | `dict[str, Any]` |
| `state` | `RunState` |

## Properties

- `state`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/tracers/log_stream.py#L169)
