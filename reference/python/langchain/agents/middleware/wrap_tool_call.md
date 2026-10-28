---
title: "wrap_tool_call"
description: "Prepend reviewer-edit guidance to the result of an edited tool call."
source: "https://reference.langchain.com/python/langchain/agents/middleware/wrap_tool_call"
category: "reference"
tags: [reference, langchain, agents, middleware, wrap_tool_call]
---

# wrap_tool_call

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/HumanInTheLoopMiddleware/wrap_tool_call)

Prepend reviewer-edit guidance to the result of an edited tool call.

In `per_call` mode this is also where the interrupt is raised.

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
| `request` | `ToolCallRequest` | Yes | The tool call request being executed. |
| `handler` | `Callable[[ToolCallRequest], ToolMessage \| Command[Any]]` | Yes | Callable that executes the tool. |

## Returns

`ToolMessage | Command[Any]`

The tool result, with a note prepended when a reviewer edited the call.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/fbb8a35da7023ac0382c3b22f047337861bd3486/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L979)
