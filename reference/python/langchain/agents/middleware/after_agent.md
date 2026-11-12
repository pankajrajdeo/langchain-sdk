---
title: "after_agent"
description: "Run shutdown commands and release resources when an agent completes."
source: "https://reference.langchain.com/python/langchain/agents/middleware/after_agent"
category: "reference"
tags: [reference, langchain, agents, middleware, after_agent]
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c2f4036e4c6ca45a8da8a42d8e07a25d2ea48b8f/libs/langchain_v1/langchain/agents/middleware/shell_tool.py#L686)
