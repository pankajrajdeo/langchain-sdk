---
title: "awrap_tool_call"
description: "Async variant of wrap_tool_call."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/ReadFileContinuationNoticeMiddleware/awrap_tool_call"
category: "reference"
tags: [reference, deepagents, profiles, harness, nvidia_nemotron_3_ultra, readfilecontinuationnoticemiddleware, awrap_tool_call]
---

# awrap_tool_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/ReadFileContinuationNoticeMiddleware/awrap_tool_call)

Async variant of `wrap_tool_call`.

## Signature

```python
awrap_tool_call(
    self,
    request: ToolCallRequest,
    handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command[Any]]],
) -> ToolMessage | Command[Any]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/18930b5463c8a0a432353db5299af280f879973f/libs/deepagents/deepagents/profiles/harness/_nvidia_nemotron_3_ultra.py#L219)
