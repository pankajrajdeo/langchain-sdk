---
title: "subagent_names"
description: "Declared subagent names. Public so streamers can discover them without introspecting the task tool's closure."
source: "https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgentMiddleware/subagent_names"
category: "reference"
tags: [reference, deepagents, middleware, subagents, subagentmiddleware, subagent_names]
---

# subagent_names

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgentMiddleware/subagent_names)

Declared subagent names. Public so streamers can discover them
without introspecting the `task` tool's closure.

## Signature

```python
subagent_names: frozenset[str] = frozenset(spec['name'] for spec in subagents)
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/middleware/subagents.py#L997)
