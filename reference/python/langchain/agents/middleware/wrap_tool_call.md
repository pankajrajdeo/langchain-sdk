---
title: "wrap_tool_call"
description: "Intercept tool execution and convert handled exceptions to error messages."
source: "https://reference.langchain.com/python/langchain/agents/middleware/wrap_tool_call"
category: "reference"
tags: [reference, langchain, agents, middleware, wrap_tool_call]
---

# wrap_tool_call

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/tool_error/ToolErrorMiddleware/wrap_tool_call)

Intercept tool execution and convert handled exceptions to error messages.

## Signature

```python
wrap_tool_call(
    self,
    request: ToolCallRequest,
    handler: Callable[[ToolCallRequest], ToolMessage | Command[Any]],
) -> ToolMessage | Command[Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | `ToolCallRequest` | Yes | Tool call request with call dict, `BaseTool`, state, and runtime. |
| `handler` | `Callable[[ToolCallRequest], ToolMessage \| Command[Any]]` | Yes | Callable to execute the tool. |

## Returns

`ToolMessage | Command[Any]`

`ToolMessage` or `Command` (the final result).

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c2f4036e4c6ca45a8da8a42d8e07a25d2ea48b8f/libs/langchain_v1/langchain/agents/middleware/tool_error.py#L133)
