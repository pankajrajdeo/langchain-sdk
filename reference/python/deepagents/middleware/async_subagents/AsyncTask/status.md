---
title: "status"
description: "Current task status (e.g., 'running', 'success', 'error', 'cancelled')."
source: "https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncTask/status"
category: "reference"
tags: [reference, deepagents, middleware, async_subagents, asynctask, status]
---

# status

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncTask/status)

Current task status (e.g., `'running'`, `'success'`, `'error'`, `'cancelled'`).

Typed as `str` rather than a `Literal` because the LangGraph SDK's
`Run.status` is `str` — using a `Literal` here would require `cast` at every
SDK boundary.

## Signature

```python
status: str
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/4394bcd00b8eb46e7c423939643a0dfcfb5d8773/libs/deepagents/deepagents/middleware/async_subagents.py#L95)
