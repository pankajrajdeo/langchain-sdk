---
title: "OnError"
description: "Sync handler: return content to surface the error as a ToolMessage; return None (or nothing) to let the exception propagate."
source: "https://reference.langchain.com/python/langchain/agents/middleware/tool_error/OnError"
category: "reference"
tags: [reference, langchain, agents, middleware, tool_error, onerror]
---

# OnError

> **Attribute** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/tool_error/OnError)

Sync handler: return content to surface the error as a `ToolMessage`; return
`None` (or nothing) to let the exception propagate.

## Signature

```python
OnError = Callable[[Exception, ToolCallRequest], str | list[ContentBlock] | None]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/5dcec1858191a6b54cd843dd8e54d856e2e007cc/libs/langchain_v1/langchain/agents/middleware/tool_error.py#L28)
