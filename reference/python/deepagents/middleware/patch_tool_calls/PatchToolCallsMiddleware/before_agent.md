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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/middleware/patch_tool_calls.py#L17)
