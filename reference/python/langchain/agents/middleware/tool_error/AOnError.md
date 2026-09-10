---
title: "AOnError"
description: "Async handler: return content to surface the error as a ToolMessage; return None (or nothing) to let the exception propagate."
source: "https://reference.langchain.com/python/langchain/agents/middleware/tool_error/AOnError"
category: "reference"
tags: [reference, langchain, agents, middleware, tool_error, aonerror]
---

# AOnError

> **Attribute** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/tool_error/AOnError)

Async handler: return content to surface the error as a `ToolMessage`; return
`None` (or nothing) to let the exception propagate.

## Signature

```python
AOnError = Callable[[Exception, ToolCallRequest], Awaitable[str | list[ContentBlock] | None]]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/middleware/tool_error.py#L32)
