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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93/libs/langgraph/langgraph/pregel/_executor.py#L222)
