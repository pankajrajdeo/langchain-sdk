---
title: "put"
description: "Put the item on the queue."
source: "https://reference.langchain.com/python/langgraph/_internal/_queue/SyncQueue/put"
category: "reference"
tags: [reference, langgraph, internal, queue, syncqueue, put]
---

# put

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_queue/SyncQueue/put)

Put the item on the queue.

The optional 'block' and 'timeout' arguments are ignored, as this method
never blocks.  They are provided for compatibility with the Queue class.

## Signature

```python
put(
    self,
    item,
    block = True,
    timeout = None,
)
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/58a6e1cc5b7dfc3619fc6e7e7573b040d554649b/libs/langgraph/langgraph/_internal/_queue.py#L79)
