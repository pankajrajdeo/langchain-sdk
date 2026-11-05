---
title: "bind"
description: "Bind additional kwargs to a Runnable, returning a new Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBinding/bind"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnablebinding, bind]
---

# bind

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBinding/bind)

Bind additional kwargs to a `Runnable`, returning a new `Runnable`.

## Signature

```python
bind(
    self,
    kwargs: Any = {},
) -> Runnable[Input, Output]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `**kwargs` | `Any` | No | The kwargs to bind to the `Runnable`. (default: `{}`) |

## Returns

`Runnable[Input, Output]`

A new `Runnable` with the same type and config as the original,

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/b4aa7e7d00c452251720ce30b8bc2c41ca44e1f5/libs/core/langchain_core/runnables/base.py#L6417)
