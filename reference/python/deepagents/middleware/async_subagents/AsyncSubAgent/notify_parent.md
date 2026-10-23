---
title: "notify_parent"
description: "Whether this subagent may wake this agent when it finishes while this agent is idle. Defaults to True."
source: "https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgent/notify_parent"
category: "reference"
tags: [reference, deepagents, middleware, async_subagents, asyncsubagent, notify_parent]
---

# notify_parent

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgent/notify_parent)

Whether this subagent may wake this agent when it finishes while this agent is idle. Defaults to `True`.

Set it to `False` when the application delivers results itself, for example
through `webhook`. This agent still sees the subagent's updates while it runs.

!!! warning "Beta"

    `notify_parent` may change along with how subagents wake their parent.

## Signature

```python
notify_parent: NotRequired[bool]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/middleware/async_subagents.py#L133)
