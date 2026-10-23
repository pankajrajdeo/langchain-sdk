---
title: "RootListenersTracer"
description: "Tracer that calls listeners on run start, end, and error."
source: "https://reference.langchain.com/python/langchain-core/tracers/root_listeners/RootListenersTracer"
category: "reference"
tags: [reference, langchain-core, tracers, root_listeners, rootlistenerstracer]
---

# RootListenersTracer

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/root_listeners/RootListenersTracer)

Tracer that calls listeners on run start, end, and error.

## Signature

```python
RootListenersTracer(
    self,
    *,
    config: RunnableConfig,
    on_start: Listener | None,
    on_end: Listener | None,
    on_error: Listener | None,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig` | Yes | The runnable config. |
| `on_start` | `Listener \| None` | Yes | The listener to call on run start. |
| `on_end` | `Listener \| None` | Yes | The listener to call on run end. |
| `on_error` | `Listener \| None` | Yes | The listener to call on run error |

## Extends

- `BaseTracer`

## Constructors

```python
__init__(
    self,
    *,
    config: RunnableConfig,
    on_start: Listener | None,
    on_end: Listener | None,
    on_error: Listener | None,
) -> None
```

| Name | Type |
|------|------|
| `config` | `RunnableConfig` |
| `on_start` | `Listener \| None` |
| `on_end` | `Listener \| None` |
| `on_error` | `Listener \| None` |

## Properties

- `log_missing_parent`
- `config`
- `root_id`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/tracers/root_listeners.py#L23)
