---
title: "coerce_to_runnable"
description: "Coerce a runnable-like object into a Runnable."
source: "https://reference.langchain.com/python/langgraph/_internal/_runnable/coerce_to_runnable"
category: "reference"
tags: [reference, langgraph, internal, runnable, coerce_to_runnable]
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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/58a6e1cc5b7dfc3619fc6e7e7573b040d554649b/libs/langgraph/langgraph/_internal/_runnable.py#L582)
