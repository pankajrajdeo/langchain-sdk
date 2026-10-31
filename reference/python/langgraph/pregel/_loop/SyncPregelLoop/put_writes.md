---
title: "put_writes"
description: "Put writes for a task, to be read by the next tick."
source: "https://reference.langchain.com/python/langgraph/pregel/_loop/SyncPregelLoop/put_writes"
category: "reference"
tags: [reference, langgraph, pregel, loop, syncpregelloop, put_writes]
---

# put_writes

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_loop/SyncPregelLoop/put_writes)

Put writes for a task, to be read by the next tick.

## Signature

```python
put_writes(
    self,
    task_id: str,
    writes: WritesT,
    *,
    cached: bool = False,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/pregel/_loop.py#L1789)
