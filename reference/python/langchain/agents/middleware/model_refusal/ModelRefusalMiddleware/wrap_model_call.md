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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c0344e0cee824c1c6489ba972cea171ff193d234/libs/langchain_v1/langchain/agents/middleware/model_refusal.py#L53)
