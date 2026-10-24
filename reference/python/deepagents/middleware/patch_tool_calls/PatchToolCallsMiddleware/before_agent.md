---
title: "before_agent"
description: "Before the agent runs, handle dangling tool calls from any AIMessage."
source: "https://reference.langchain.com/python/deepagents/middleware/patch_tool_calls/PatchToolCallsMiddleware/before_agent"
category: "reference"
tags: [reference, deepagents, middleware, patch_tool_calls, patchtoolcallsmiddleware, before_agent]
---

# before_agent

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/patch_tool_calls/PatchToolCallsMiddleware/before_agent)

Before the agent runs, handle dangling tool calls from any AIMessage.

## Signature

```python
before_agent(
    self,
    state: AgentState,
    runtime: Runtime[Any],
) -> dict[str, Any] | None
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/middleware/patch_tool_calls.py#L17)
