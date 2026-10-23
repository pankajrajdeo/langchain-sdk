---
title: "CONTROL_WRITES"
description: "Channels that describe what happened to a task rather than what it produced."
source: "https://reference.langchain.com/python/langgraph/pregel/_task_status/CONTROL_WRITES"
category: "reference"
tags: [reference, langgraph, pregel, task_status, control_writes]
---

# CONTROL_WRITES

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_task_status/CONTROL_WRITES)

Channels that describe what happened to a task rather than what it produced.

## Signature

```python
CONTROL_WRITES = frozenset((ERROR, ERROR_SOURCE_NODE, INTERRUPT, RESUME))
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/pregel/_task_status.py#L71)
