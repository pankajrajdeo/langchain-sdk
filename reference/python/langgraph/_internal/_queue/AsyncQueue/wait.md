---
title: "wait"
description: "If queue is empty, wait until an item is available."
source: "https://reference.langchain.com/python/langgraph/_internal/_queue/AsyncQueue/wait"
category: "reference"
tags: [reference, langgraph, internal, queue, asyncqueue, wait]
---

# wait

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_queue/AsyncQueue/wait)

If queue is empty, wait until an item is available.

Copied from Queue.get(), removing the call to .get_nowait(),
ie. this doesn't consume the item, just waits for it.

## Signature

```python
wait(
    self,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/langgraph/langgraph/_internal/_queue.py#L17)
