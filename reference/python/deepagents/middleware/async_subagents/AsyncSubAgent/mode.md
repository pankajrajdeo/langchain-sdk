---
title: "mode"
description: "When using mode=\"fork\", configure the remote agent to match the parent's model, system prompt, tools, and prompt-processing middleware if you want prompt-cache reuse. Fork mode copies conversation..."
source: "https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgent/mode"
category: "reference"
tags: [reference, deepagents, middleware, async_subagents, asyncsubagent, mode]
---

# mode

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgent/mode)

When using `mode="fork"`, configure the remote agent to match the parent's model,
system prompt, tools, and prompt-processing middleware if you want prompt-cache
reuse. Fork mode copies conversation history; it does not synchronize those
settings. Matching configuration is necessary but not sufficient: the rendered
prefix must match, and cache hits depend on the provider.

- `isolated` (default): send only the delegated task description.
- `fork`: send a snapshot of the parent's conversation at launch, followed
    by the task description, for background work.

Different configurations are supported for context sharing, but you should
not expect parent-to-child cache reuse with them.

!!! warning "Experimental"

    `mode="fork"` is experimental and may change in a future release.

## Signature

```python
mode: NotRequired[Literal['isolated', 'fork']]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/middleware/async_subagents.py#L144)
