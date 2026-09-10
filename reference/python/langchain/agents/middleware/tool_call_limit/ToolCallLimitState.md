---
title: "ToolCallLimitState"
description: "State schema for ToolCallLimitMiddleware."
source: "https://reference.langchain.com/python/langchain/agents/middleware/tool_call_limit/ToolCallLimitState"
category: "reference"
tags: [reference, langchain, agents, middleware, tool_call_limit, toolcalllimitstate]
---

# ToolCallLimitState

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/tool_call_limit/ToolCallLimitState)

State schema for `ToolCallLimitMiddleware`.

Extends `AgentState` with tool call tracking fields.

The count fields are dictionaries mapping tool names to execution counts. This
allows multiple middleware instances to track different tools independently. The
special key `'__all__'` is used for tracking all tool calls globally.

## Signature

```python
ToolCallLimitState()
```

## Extends

- `AgentState[ResponseT]`

## Properties

- `thread_tool_call_count`
- `run_tool_call_count`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/middleware/tool_call_limit.py#L36)
