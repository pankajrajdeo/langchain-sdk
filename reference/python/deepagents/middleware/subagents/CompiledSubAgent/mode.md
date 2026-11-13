---
title: "mode"
description: "Use fork to inherit the parent's conversation without changing the runnable prompt."
source: "https://reference.langchain.com/python/deepagents/middleware/subagents/CompiledSubAgent/mode"
category: "reference"
tags: [reference, deepagents, middleware, subagents, compiledsubagent, mode]
---

# mode

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/subagents/CompiledSubAgent/mode)

Use `fork` to inherit the parent's conversation without changing the runnable prompt.

A declarative [`SubAgent`][deepagents.middleware.subagents.SubAgent] fork
inherits the full state, including private keys.

## Signature

```python
mode: NotRequired[Literal['isolated', 'fork']]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0ec42441901968a75202a3ef365650eb280a473b/libs/deepagents/deepagents/middleware/subagents.py#L348)
