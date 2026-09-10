---
title: "wrap_tool_call"
description: "Intercept tool execution and retry on failure."
source: "https://reference.langchain.com/python/langchain/agents/middleware/tool_retry/ToolRetryMiddleware/wrap_tool_call"
category: "reference"
tags: [reference, langchain, agents, middleware, tool_retry, toolretrymiddleware, wrap_tool_call]
---

# wrap_tool_call

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/tool_retry/ToolRetryMiddleware/wrap_tool_call)

Intercept tool execution and retry on failure.

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
| `handler` | `Callable[[ToolCallRequest], ToolMessage \| Command[Any]]` | Yes | Callable to execute the tool (can be called multiple times). |

## Returns

`ToolMessage | Command[Any]`

`ToolMessage` or `Command` (the final result).

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/middleware/tool_retry.py#L295)
