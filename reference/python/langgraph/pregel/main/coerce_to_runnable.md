---
title: "coerce_to_runnable"
description: "Coerce a runnable-like object into a Runnable."
source: "https://reference.langchain.com/python/langgraph/pregel/main/coerce_to_runnable"
category: "reference"
tags: [reference, langgraph, pregel, main, coerce_to_runnable]
---

# coerce_to_runnable

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_runnable/coerce_to_runnable)

Coerce a runnable-like object into a Runnable.

## Signature

```python
coerce_to_runnable(
    thing: RunnableLike,
    *,
    name: str | None,
    trace: bool,
) -> Runnable
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thing` | `RunnableLike` | Yes | A runnable-like object. |

## Returns

`Runnable`

A Runnable.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/langgraph/langgraph/_internal/_runnable.py#L550)
