---
title: "timeout"
description: "Timeout policy for a single invocation."
source: "https://reference.langchain.com/python/langgraph/pregel/_read/PregelNode/timeout"
category: "reference"
tags: [reference, langgraph, pregel, read, pregelnode, timeout]
---

# timeout

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_read/PregelNode/timeout)

Timeout policy for a single invocation.

If exceeded, `NodeTimeoutError` is raised and the retry policy (if any)
decides whether to retry. Supported only for async nodes.

## Signature

```python
timeout: TimeoutPolicy | None = coerce_timeout_policy(timeout)
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/pregel/_read.py#L181)
