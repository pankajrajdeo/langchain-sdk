---
title: "status"
description: "Current task status (e.g., 'pending', 'running', 'waiting', 'success', 'error', 'cancelled')."
source: "https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncTask/status"
category: "reference"
tags: [reference, deepagents, middleware, async_subagents, asynctask, status]
---

# status

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncTask/status)

Current task status (e.g., `'pending'`, `'running'`, `'waiting'`, `'success'`, `'error'`, `'cancelled'`).

`'pending'` means the latest run hasn't started yet. After a queued follow-up,
an earlier run may still be working.

Typed as `str` rather than a `Literal` because the LangGraph SDK's
`Run.status` is `str` — using a `Literal` here would require `cast` at every
SDK boundary.

!!! warning "Beta"

    `'waiting'` means the subagent paused for its user (an approval or a
    question), who answers it on the subagent's own thread. This may change.

## Signature

```python
status: str
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/middleware/async_subagents.py#L204)
