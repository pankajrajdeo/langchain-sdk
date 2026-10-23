---
title: "status_filter"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/deepagents/middleware/async_subagents/ListAsyncTasksSchema/status_filter"
category: "reference"
tags: [reference, deepagents, middleware, async_subagents, listasynctasksschema, status_filter]
---

# status_filter

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/async_subagents/ListAsyncTasksSchema/status_filter)

## Signature

```python
status_filter: Literal['running', 'pending', 'waiting', 'success', 'error', 'cancelled', 'all'] | None = Field(default=None, description="Filter tasks by status. One of: 'running', 'pending', 'waiting', 'success', 'error', 'cancelled', 'all'. Defaults to 'all'.")
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/middleware/async_subagents.py#L284)
