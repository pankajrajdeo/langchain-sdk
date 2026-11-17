---
title: "tools"
description: "Tools the subagent can use."
source: "https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgent/tools"
category: "reference"
tags: [reference, deepagents, middleware, subagents, subagent, tools]
---

# tools

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgent/tools)

Tools the subagent can use.

If not specified, inherits tools from the main agent via `default_tools`.

## Signature

```python
tools: NotRequired[Sequence[BaseTool | Callable | dict[str, Any]]]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/53e090968118f72f6dd3847d097607461a0fb5a8/libs/deepagents/deepagents/middleware/subagents.py#L149)
