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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/53e090968118f72f6dd3847d097607461a0fb5a8/libs/deepagents/deepagents/middleware/patch_tool_calls.py#L17)
