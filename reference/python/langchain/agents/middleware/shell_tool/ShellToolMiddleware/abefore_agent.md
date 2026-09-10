---
title: "abefore_agent"
description: "Async start the shell session and run startup commands."
source: "https://reference.langchain.com/python/langchain/agents/middleware/shell_tool/ShellToolMiddleware/abefore_agent"
category: "reference"
tags: [reference, langchain, agents, middleware, shell_tool, shelltoolmiddleware, abefore_agent]
---

# abefore_agent

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/shell_tool/ShellToolMiddleware/abefore_agent)

Async start the shell session and run startup commands.

## Signature

```python
abefore_agent(
    self,
    state: ShellToolState[ResponseT],
    runtime: Runtime[ContextT],
) -> dict[str, Any] | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `state` | `ShellToolState[ResponseT]` | Yes | The current agent state. |
| `runtime` | `Runtime[ContextT]` | Yes | The runtime context. |

## Returns

`dict[str, Any] | None`

Shell session resources to be stored in the agent state.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/middleware/shell_tool.py#L672)
