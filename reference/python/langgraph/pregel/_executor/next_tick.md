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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/pregel/_executor.py#L228)
