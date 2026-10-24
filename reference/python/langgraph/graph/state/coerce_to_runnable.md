---
title: "coerce_to_runnable"
description: "Coerce a runnable-like object into a Runnable."
source: "https://reference.langchain.com/python/langgraph/graph/state/coerce_to_runnable"
category: "reference"
tags: [reference, langgraph, graph, state, coerce_to_runnable]
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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/_internal/_runnable.py#L550)
