---
title: "get"
description: "Remove and return an item from the queue."
source: "https://reference.langchain.com/python/langgraph/_internal/_queue/SyncQueue/get"
category: "reference"
tags: [reference, langgraph, internal, queue, syncqueue, get]
---

# get

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_queue/SyncQueue/get)

Remove and return an item from the queue.

If optional args 'block' is true and 'timeout' is None (the default),
block if necessary until an item is available. If 'timeout' is
a non-negative number, it blocks at most 'timeout' seconds and raises
the Empty exception if no item was available within that time.
Otherwise ('block' is false), return an item if one is immediately
available, else raise the Empty exception ('timeout' is ignored
in that case).

## Signature

```python
get(
    self,
    block = False,
    timeout = None,
)
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/_internal/_queue.py#L88)
