---
title: "wrap_model_call"
description: "Check the completed synchronous model response for a refusal."
source: "https://reference.langchain.com/python/langchain/agents/middleware/model_refusal/ModelRefusalMiddleware/wrap_model_call"
category: "reference"
tags: [reference, langchain, agents, middleware, model_refusal, modelrefusalmiddleware, wrap_model_call]
---

# wrap_model_call

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/model_refusal/ModelRefusalMiddleware/wrap_model_call)

Check the completed synchronous model response for a refusal.

## Signature

```python
wrap_model_call(
    self,
    request: ModelRequest[ContextT],
    handler: Callable[[ModelRequest[ContextT]], ModelResponse[ResponseT]],
) -> ModelResponse[ResponseT]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d1d95b79213b0212613ae1aa4fad38bea6f1dccf/libs/langchain_v1/langchain/agents/middleware/model_refusal.py#L49)
