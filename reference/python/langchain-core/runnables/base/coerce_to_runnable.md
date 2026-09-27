---
title: "coerce_to_runnable"
description: "Coerce a Runnable-like object into a Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/coerce_to_runnable"
category: "reference"
tags: [reference, langchain-core, runnables, base, coerce_to_runnable]
---

# coerce_to_runnable

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/coerce_to_runnable)

Coerce a `Runnable`-like object into a `Runnable`.

## Signature

```python
coerce_to_runnable(
    thing: RunnableLike[Input, Output],
) -> Runnable[Input, Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thing` | `RunnableLike[Input, Output]` | Yes | A `Runnable`-like object. |

## Returns

`Runnable[Input, Any]`

A `Runnable`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/runnables/base.py#L6640)
