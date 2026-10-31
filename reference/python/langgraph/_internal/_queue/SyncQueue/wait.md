---
title: "wait"
description: "If queue is empty, wait until an item maybe is available, but don't consume it."
source: "https://reference.langchain.com/python/langgraph/_internal/_queue/SyncQueue/wait"
category: "reference"
tags: [reference, langgraph, internal, queue, syncqueue, wait]
---

# wait

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_queue/SyncQueue/wait)

If queue is empty, wait until an item maybe is available,
but don't consume it.

## Signature

```python
wait(
    self,
    block = True,
    timeout = None,
)
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/_internal/_queue.py#L108)
