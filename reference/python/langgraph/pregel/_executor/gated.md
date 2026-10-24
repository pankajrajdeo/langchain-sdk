---
title: "gated"
description: "A coroutine that waits for a semaphore before running another coroutine."
source: "https://reference.langchain.com/python/langgraph/pregel/_executor/gated"
category: "reference"
tags: [reference, langgraph, pregel, executor, gated]
---

# gated

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_executor/gated)

A coroutine that waits for a semaphore before running another coroutine.

## Signature

```python
gated(
    semaphore: asyncio.Semaphore,
    coro: Coroutine[None, None, T],
) -> T
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/pregel/_executor.py#L214)
