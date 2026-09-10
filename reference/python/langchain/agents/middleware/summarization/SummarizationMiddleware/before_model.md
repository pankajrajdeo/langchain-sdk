---
title: "before_model"
description: "Process messages before model invocation, potentially triggering summarization."
source: "https://reference.langchain.com/python/langchain/agents/middleware/summarization/SummarizationMiddleware/before_model"
category: "reference"
tags: [reference, langchain, agents, middleware, summarization, summarizationmiddleware, before_model]
---

# before_model

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/summarization/SummarizationMiddleware/before_model)

Process messages before model invocation, potentially triggering summarization.

## Signature

```python
before_model(
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/middleware/summarization.py#L397)
