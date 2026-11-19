---
title: "before_model"
description: "Process messages before model invocation, potentially triggering summarization."
source: "https://reference.langchain.com/python/langchain/agents/middleware/before_model"
category: "reference"
tags: [reference, langchain, agents, middleware, before_model]
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ced9bdb1a8899516b6c541fc0e19ab5f349aa0ea/libs/langchain_v1/langchain/agents/middleware/summarization.py#L478)
