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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9b754bc914cc75c3f6d8c6e99353e81041b73bce/libs/deepagents/deepagents/middleware/subagents.py#L149)
