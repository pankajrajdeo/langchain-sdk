---
title: "wrap_tool_call"
description: "Annotate read_file results that may have more pages."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/ReadFileContinuationNoticeMiddleware/wrap_tool_call"
category: "reference"
tags: [reference, deepagents, profiles, harness, nvidia_nemotron_3_ultra, readfilecontinuationnoticemiddleware, wrap_tool_call]
---

# wrap_tool_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/ReadFileContinuationNoticeMiddleware/wrap_tool_call)

Annotate `read_file` results that may have more pages.

## Signature

```python
wrap_tool_call(
    self,
    request: ToolCallRequest,
    handler: Callable[[ToolCallRequest], ToolMessage | Command[Any]],
) -> ToolMessage | Command[Any]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/18930b5463c8a0a432353db5299af280f879973f/libs/deepagents/deepagents/profiles/harness/_nvidia_nemotron_3_ultra.py#L211)
