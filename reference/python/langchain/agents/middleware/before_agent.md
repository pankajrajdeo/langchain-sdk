---
title: "before_agent"
description: "Start the shell session and run startup commands."
source: "https://reference.langchain.com/python/langchain/agents/middleware/before_agent"
category: "reference"
tags: [reference, langchain, agents, middleware, before_agent]
---

# before_agent

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/shell_tool/ShellToolMiddleware/before_agent)

Start the shell session and run startup commands.

## Signature

```python
before_agent(
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/middleware/shell_tool.py#L656)
