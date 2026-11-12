---
title: "ExitBehavior"
description: "How to handle execution when tool call limits are exceeded."
source: "https://reference.langchain.com/python/langchain/agents/middleware/tool_call_limit/ExitBehavior"
category: "reference"
tags: [reference, langchain, agents, middleware, tool_call_limit, exitbehavior]
---

# ExitBehavior

> **Attribute** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/tool_call_limit/ExitBehavior)

How to handle execution when tool call limits are exceeded.

- `'continue'`: Block exceeded tools with error messages, let other tools continue
    (default)
- `'error'`: Raise a `ToolCallLimitExceededError` exception
- `'end'`: Stop execution immediately, injecting a `ToolMessage` for each tool call
    that exceeded the limit and an `AIMessage` explaining why. Any other pending tool
    call on the same `AIMessage` (e.g. from parallel tool calling) also gets an
    explanatory `ToolMessage` instead of being executed.

## Signature

```python
ExitBehavior = Literal['continue', 'error', 'end']
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c2f4036e4c6ca45a8da8a42d8e07a25d2ea48b8f/libs/langchain_v1/langchain/agents/middleware/tool_call_limit.py#L23)
