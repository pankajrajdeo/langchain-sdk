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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/pregel/_loop.py#L1819)
