---
title: "next_tick"
description: "A function that yields control to other threads before running another function."
source: "https://reference.langchain.com/python/langgraph/pregel/_executor/next_tick"
category: "reference"
tags: [reference, langgraph, pregel, executor, next_tick]
---

# next_tick

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_executor/next_tick)

A function that yields control to other threads before running another function.

## Signature

```python
next_tick(
    fn: Callable[P, T],
    args: P.args = (),
    kwargs: P.kwargs = {},
) -> T
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/pregel/_executor.py#L228)
