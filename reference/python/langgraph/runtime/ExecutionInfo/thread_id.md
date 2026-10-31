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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/runtime.py#L39)
