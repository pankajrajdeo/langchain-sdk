---
title: "RunLogPatch"
description: "Patch to the run log."
source: "https://reference.langchain.com/python/langchain-core/tracers/log_stream/RunLogPatch"
category: "reference"
tags: [reference, langchain-core, tracers, log_stream, runlogpatch]
---

# RunLogPatch

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/log_stream/RunLogPatch)

Patch to the run log.

## Signature

```python
RunLogPatch(
    self,
    ops: dict[str, Any] = (),
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `*ops` | `dict[str, Any]` | No | The operations to apply to the state. (default: `()`) |

## Constructors

```python
__init__(
    self,
    ops: dict[str, Any] = (),
) -> None
```

| Name | Type |
|------|------|
| `ops` | `dict[str, Any]` |

## Properties

- `ops`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d4dafe5839c4a6b07d71cc78697df0de9e627e21/libs/core/langchain_core/tracers/log_stream.py#L116)
