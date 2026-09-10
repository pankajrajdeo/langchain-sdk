---
title: "abefore_agent"
description: "Load memory content before agent execution."
source: "https://reference.langchain.com/python/deepagents/middleware/memory/MemoryMiddleware/abefore_agent"
category: "reference"
tags: [reference, deepagents, middleware, memory, memorymiddleware, abefore_agent]
---

# abefore_agent

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/memory/MemoryMiddleware/abefore_agent)

Load memory content before agent execution.

Loads memory from all configured sources and stores in state.
Only loads if not already present in state.

## Signature

```python
abefore_agent(
    self,
    state: MemoryState,
    runtime: Runtime,
    config: RunnableConfig,
) -> MemoryStateUpdate | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `state` | `MemoryState` | Yes | Current agent state. |
| `runtime` | `Runtime` | Yes | Runtime context. |
| `config` | `RunnableConfig` | Yes | Runnable config. |

## Returns

`MemoryStateUpdate | None`

State update with memory_contents populated.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/middleware/memory.py#L313)
