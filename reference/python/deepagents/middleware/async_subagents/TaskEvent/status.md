---
title: "status"
description: "waiting means the subagent paused for input or approval; cancelled, that its run was cancelled on the server."
source: "https://reference.langchain.com/python/deepagents/middleware/async_subagents/TaskEvent/status"
category: "reference"
tags: [reference, deepagents, middleware, async_subagents, taskevent, status]
---

# status

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/async_subagents/TaskEvent/status)

`waiting` means the subagent paused for input or approval; `cancelled`, that its run was cancelled on the server.

## Signature

```python
status: Literal['success', 'error', 'timeout', 'cancelled', 'waiting']
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9ea3f1912abd8b7eecb504d78ef99fcf279bf561/libs/deepagents/deepagents/middleware/async_subagents.py#L495)
