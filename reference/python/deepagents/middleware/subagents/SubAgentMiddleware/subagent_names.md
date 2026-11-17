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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/53e090968118f72f6dd3847d097607461a0fb5a8/libs/deepagents/deepagents/middleware/subagents.py#L1114)
