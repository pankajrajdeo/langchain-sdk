---
title: "after_agent"
description: "Run shutdown commands and release resources when an agent completes."
source: "https://reference.langchain.com/python/langchain/agents/middleware/shell_tool/ShellToolMiddleware/after_agent"
category: "reference"
tags: [reference, langchain, agents, middleware, shell_tool, shelltoolmiddleware, after_agent]
---

# after_agent

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/shell_tool/ShellToolMiddleware/after_agent)

Run shutdown commands and release resources when an agent completes.

## Signature

```python
after_agent(
    self,
    state: ShellToolState[ResponseT],
    runtime: Runtime[ContextT],
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d1d95b79213b0212613ae1aa4fad38bea6f1dccf/libs/langchain_v1/langchain/agents/middleware/shell_tool.py#L686)
