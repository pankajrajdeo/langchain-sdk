---
title: "modify_request"
description: "Inject memory content into the system message."
source: "https://reference.langchain.com/python/deepagents/middleware/memory/MemoryMiddleware/modify_request"
category: "reference"
tags: [reference, deepagents, middleware, memory, memorymiddleware, modify_request]
---

# modify_request

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/memory/MemoryMiddleware/modify_request)

Inject memory content into the system message.

## Signature

```python
modify_request(
    self,
    request: ModelRequest[ContextT],
) -> ModelRequest[ContextT]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | `ModelRequest[ContextT]` | Yes | Model request to modify. |

## Returns

`ModelRequest[ContextT]`

Modified request with memory injected into system message.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/middleware/memory.py#L347)
