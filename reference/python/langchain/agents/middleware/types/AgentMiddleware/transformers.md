---
title: "transformers"
description: "Stream transformer factories registered by the middleware."
source: "https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/transformers"
category: "reference"
tags: [reference, langchain, agents, middleware, types, agentmiddleware, transformers]
---

# transformers

> **Attribute** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentMiddleware/transformers)

Stream transformer factories registered by the middleware.

Each entry is a scope-aware factory invoked as `factory(scope)` so every
invocation receives a fresh instance. Factories are merged with the
`transformers` argument of [`create_agent`][langchain.agents.create_agent]
at graph compile time, after the `ToolCallTransformer` and before any
user-supplied entries.

## Signature

```python
transformers: Sequence[TransformerFactory] = ()
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/be854a130153e51346d83d3b06f959b80f6cbca6/libs/langchain_v1/langchain/agents/middleware/types.py#L413)
