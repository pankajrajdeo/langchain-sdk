---
title: "put_writes"
description: "Put writes for a task, to be read by the next tick."
source: "https://reference.langchain.com/python/langgraph/pregel/_loop/AsyncPregelLoop/put_writes"
category: "reference"
tags: [reference, langgraph, pregel, loop, asyncpregelloop, put_writes]
---

# put_writes

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_loop/AsyncPregelLoop/put_writes)

Put writes for a task, to be read by the next tick.

## Signature

```python
put_writes(
    self,
    task_id: str,
    writes: WritesT,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/pregel/_loop.py#L1864)
