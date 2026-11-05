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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/pregel/_executor.py#L222)
