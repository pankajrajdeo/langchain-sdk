---
title: "superseded_run_ids"
description: "Earlier runs of this task, oldest first, from before a queued follow-up."
source: "https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncTask/superseded_run_ids"
category: "reference"
tags: [reference, deepagents, middleware, async_subagents, asynctask, superseded_run_ids]
---

# superseded_run_ids

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncTask/superseded_run_ids)

Earlier runs of this task, oldest first, from before a queued follow-up.

Their notifications don't complete the task, and cancelling the task also
cancels any that are still active. Set only with `update_strategy='enqueue'`.

## Signature

```python
superseded_run_ids: NotRequired[list[str]]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/middleware/async_subagents.py#L197)
