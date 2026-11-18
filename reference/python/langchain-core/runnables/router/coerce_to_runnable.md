---
title: "coerce_to_runnable"
description: "Coerce a Runnable-like object into a Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/router/coerce_to_runnable"
category: "reference"
tags: [reference, langchain-core, runnables, router, coerce_to_runnable]
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/5069b326c53069ec85a7e1d914c6873feb8d0cfa/libs/core/langchain_core/runnables/base.py#L6627)
