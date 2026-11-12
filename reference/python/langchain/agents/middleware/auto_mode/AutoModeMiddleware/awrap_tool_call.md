---
title: "awrap_tool_call"
description: "Asynchronously execute a low-risk tool call or return a blocked result."
source: "https://reference.langchain.com/python/langchain/agents/middleware/auto_mode/AutoModeMiddleware/awrap_tool_call"
category: "reference"
tags: [reference, langchain, agents, middleware, auto_mode, automodemiddleware, awrap_tool_call]
---

# awrap_tool_call

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/auto_mode/AutoModeMiddleware/awrap_tool_call)

Asynchronously execute a low-risk tool call or return a blocked result.

## Signature

```python
awrap_tool_call(
    self,
    request: ToolCallRequest,
    handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command[Any]]],
) -> ToolMessage | Command[Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | `ToolCallRequest` | Yes | Tool call request and current agent state. |
| `handler` | `Callable[[ToolCallRequest], Awaitable[ToolMessage \| Command[Any]]]` | Yes | Async callable that executes the tool. |

## Returns

`ToolMessage | Command[Any]`

The tool result for a low-risk call, or an error `ToolMessage` when blocked.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c2f4036e4c6ca45a8da8a42d8e07a25d2ea48b8f/libs/langchain_v1/langchain/agents/middleware/auto_mode.py#L206)
