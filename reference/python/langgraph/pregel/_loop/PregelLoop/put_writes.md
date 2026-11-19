---
title: "put_writes"
description: "Put writes for a task, to be read by the next tick."
source: "https://reference.langchain.com/python/langgraph/pregel/_loop/PregelLoop/put_writes"
category: "reference"
tags: [reference, langgraph, pregel, loop, pregelloop, put_writes]
---

# put_writes

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_loop/PregelLoop/put_writes)

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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93/libs/langgraph/langgraph/pregel/_loop.py#L471)
