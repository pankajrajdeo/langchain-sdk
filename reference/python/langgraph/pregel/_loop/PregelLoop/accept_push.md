---
title: "accept_push"
description: "Accept a PUSH from a task, potentially returning a new task to start."
source: "https://reference.langchain.com/python/langgraph/pregel/_loop/PregelLoop/accept_push"
category: "reference"
tags: [reference, langgraph, pregel, loop, pregelloop, accept_push]
---

# accept_push

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_loop/PregelLoop/accept_push)

Accept a PUSH from a task, potentially returning a new task to start.

## Signature

```python
accept_push(
    self,
    task: PregelExecutableTask,
    write_idx: int,
    call: Call | None = None,
) -> PregelExecutableTask | None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/pregel/_loop.py#L601)
