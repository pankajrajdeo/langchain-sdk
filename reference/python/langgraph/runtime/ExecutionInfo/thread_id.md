---
title: "thread_id"
description: "The thread ID for the current execution."
source: "https://reference.langchain.com/python/langgraph/runtime/ExecutionInfo/thread_id"
category: "reference"
tags: [reference, langgraph, runtime, executioninfo, thread_id]
---

# thread_id

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/runtime/ExecutionInfo/thread_id)

The thread ID for the current execution.

None when running without a checkpointer (i.e., no persistence).

## Signature

```python
thread_id: str | None = None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/langgraph/langgraph/runtime.py#L39)
