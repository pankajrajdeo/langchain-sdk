---
title: "awrap_tool_call"
description: "Run a disclosed skill tool; calls to any other unregistered tool fail as invalid (async version)."
source: "https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/awrap_tool_call"
category: "reference"
tags: [reference, deepagents, middleware, skills, skillsmiddleware, awrap_tool_call]
---

# awrap_tool_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/awrap_tool_call)

Run a disclosed skill tool; calls to any other unregistered tool fail as invalid (async version).

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
| `request` | `ToolCallRequest` | Yes | Tool call request being processed |
| `handler` | `Callable[[ToolCallRequest], Awaitable[ToolMessage \| Command[Any]]]` | Yes | Async handler function to call with the request, with any disclosed skill tool attached |

## Returns

`ToolMessage | Command[Any]`

The tool's result, or the tool node's invalid-tool error.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/middleware/skills.py#L1395)
