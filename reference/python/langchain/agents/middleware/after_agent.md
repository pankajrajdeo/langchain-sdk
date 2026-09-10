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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/middleware/shell_tool.py#L686)
