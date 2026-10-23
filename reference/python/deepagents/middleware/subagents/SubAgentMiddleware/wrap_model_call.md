---
title: "wrap_model_call"
description: "Update the system message to include instructions on using subagents."
source: "https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgentMiddleware/wrap_model_call"
category: "reference"
tags: [reference, deepagents, middleware, subagents, subagentmiddleware, wrap_model_call]
---

# wrap_model_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgentMiddleware/wrap_model_call)

Update the system message to include instructions on using subagents.

## Signature

```python
wrap_model_call(
    self,
    request: ModelRequest[ContextT],
    handler: Callable[[ModelRequest[ContextT]], ModelResponse[ResponseT]],
) -> ModelResponse[ResponseT]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/middleware/subagents.py#L1040)
