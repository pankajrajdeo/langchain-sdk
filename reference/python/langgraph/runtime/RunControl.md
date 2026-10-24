---
title: "RunControl"
description: "Run-scoped control surface for cooperative draining."
source: "https://reference.langchain.com/python/langgraph/runtime/RunControl"
category: "reference"
tags: [reference, langgraph, runtime, runcontrol]
---

# RunControl

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/runtime/RunControl)

Run-scoped control surface for cooperative draining.

Intended for a single graph run. Create a fresh `RunControl` per run;
reusing a control after `request_drain()` leaves it drained.

Safe to call from any thread: the drain request is represented by a
single attribute write, so no lock is needed for this signal.
If more mutable state is added here, add synchronization.

## Signature

```python
RunControl(
    self,
)
```

## Constructors

```python
__init__(
    self,
) -> None
```

## Properties

- `drain_requested`
- `drain_reason`

## Methods

- [`request_drain()`](https://reference.langchain.com/python/langgraph/runtime/RunControl/request_drain)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/runtime.py#L79)
