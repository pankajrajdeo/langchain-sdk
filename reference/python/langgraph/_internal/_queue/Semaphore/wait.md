---
title: "wait"
description: "Block until the semaphore can be acquired, but don't acquire it."
source: "https://reference.langchain.com/python/langgraph/_internal/_queue/Semaphore/wait"
category: "reference"
tags: [reference, langgraph, internal, queue, semaphore, wait]
---

# wait

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_queue/Semaphore/wait)

Block until the semaphore can be acquired, but don't acquire it.

## Signature

```python
wait(
    self,
    blocking: bool = True,
    timeout: float | None = None,
)
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/langgraph/langgraph/_internal/_queue.py#L47)
