---
title: "abefore_model"
description: "Process messages before model invocation, potentially triggering summarization."
source: "https://reference.langchain.com/python/langchain/agents/middleware/summarization/SummarizationMiddleware/abefore_model"
category: "reference"
tags: [reference, langchain, agents, middleware, summarization, summarizationmiddleware, abefore_model]
---

# abefore_model

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/summarization/SummarizationMiddleware/abefore_model)

Process messages before model invocation, potentially triggering summarization.

## Signature

```python
abefore_model(
    self,
    state: AgentState[Any],
    runtime: Runtime[ContextT],
) -> dict[str, Any] | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `state` | `AgentState[Any]` | Yes | The agent state. |
| `runtime` | `Runtime[ContextT]` | Yes | The runtime environment. |

## Returns

`dict[str, Any] | None`

An updated state with summarized messages if summarization was performed.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c0344e0cee824c1c6489ba972cea171ff193d234/libs/langchain_v1/langchain/agents/middleware/summarization.py#L519)
