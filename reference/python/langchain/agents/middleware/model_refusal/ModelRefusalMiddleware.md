---
title: "ModelRefusalMiddleware"
description: "Raise ModelRefusalError for responses containing a standard refusal block."
source: "https://reference.langchain.com/python/langchain/agents/middleware/model_refusal/ModelRefusalMiddleware"
category: "reference"
tags: [reference, langchain, agents, middleware, model_refusal, modelrefusalmiddleware]
---

# ModelRefusalMiddleware

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/model_refusal/ModelRefusalMiddleware)

Raise `ModelRefusalError` for responses containing a standard refusal block.

Add this middleware to `create_agent` to treat a refusal as an error instead of
a successful final answer. Model calls without this middleware continue to
return messages, including refusal content.

List it after `ModelFallbackMiddleware` so the fallback can catch the error.
Streaming content may already have been emitted before the refusal is known.
This middleware does not infer refusals from text or retry blocked requests.

## Signature

```python
ModelRefusalMiddleware()
```

## Extends

- `AgentMiddleware[AgentState[ResponseT], ContextT, ResponseT]`

## Properties

- `trace_policy`

## Methods

- [`wrap_model_call()`](https://reference.langchain.com/python/langchain/agents/middleware/model_refusal/ModelRefusalMiddleware/wrap_model_call)
- [`awrap_model_call()`](https://reference.langchain.com/python/langchain/agents/middleware/model_refusal/ModelRefusalMiddleware/awrap_model_call)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c0344e0cee824c1c6489ba972cea171ff193d234/libs/langchain_v1/langchain/agents/middleware/model_refusal.py#L39)
