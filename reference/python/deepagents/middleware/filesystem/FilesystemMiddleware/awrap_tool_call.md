---
title: "awrap_tool_call"
description: "(async) Provide on-demand media access and evict oversized tool results."
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware/awrap_tool_call"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, filesystemmiddleware, awrap_tool_call]
---

# awrap_tool_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware/awrap_tool_call)

(async) Provide on-demand media access and evict oversized tool results.

## Signature

```python
awrap_tool_call(
    self,
    request: ToolCallRequest,
    handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command]],
) -> ToolMessage | Command
```

## Description

**Note:**

Tool-execution exceptions (including `ToolException`) propagate
through this wrapper unhandled by design.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | `ToolCallRequest` | Yes | The tool call request being processed. |
| `handler` | `Callable[[ToolCallRequest], Awaitable[ToolMessage \| Command]]` | Yes | The handler function to call with the modified request. |

## Returns

`ToolMessage | Command`

The raw `ToolMessage`, or a pseudo tool message with the `ToolResult` in state.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/18930b5463c8a0a432353db5299af280f879973f/libs/deepagents/deepagents/middleware/filesystem.py#L3924)
