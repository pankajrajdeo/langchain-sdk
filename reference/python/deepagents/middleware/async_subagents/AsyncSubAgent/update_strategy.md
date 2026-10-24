---
title: "update_strategy"
description: "How update_async_task sends a follow-up while a run is active. Defaults to 'interrupt'."
source: "https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgent/update_strategy"
category: "reference"
tags: [reference, deepagents, middleware, async_subagents, asyncsubagent, update_strategy]
---

# update_strategy

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgent/update_strategy)

How `update_async_task` sends a follow-up while a run is active. Defaults to `'interrupt'`.

- `interrupt`: stop the current run and start the follow-up.
- `enqueue`: queue the follow-up behind the current run. The task is `pending`
    until the follow-up starts. If the current run stops to ask its user for
    approval or input, the follow-up still starts, and that request is dropped.

!!! warning "Beta"

    `update_strategy` may change along with how queued follow-ups are tracked.

## Signature

```python
update_strategy: NotRequired[Literal['interrupt', 'enqueue']]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/middleware/async_subagents.py#L120)
