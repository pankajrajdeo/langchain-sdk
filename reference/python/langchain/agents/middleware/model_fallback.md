---
title: "model_fallback"
description: "Model fallback middleware for agents."
source: "https://reference.langchain.com/python/langchain/agents/middleware/model_fallback"
category: "reference"
tags: [reference, langchain, agents, middleware, model_fallback]
---

# model_fallback

> **Module** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/model_fallback)

Model fallback middleware for agents.

When an outer caching middleware modifies a request, those changes happen before
the fallback loop runs. Provider-specific cache settings can cause API errors if
the loop reuses them with a different provider. This middleware therefore strips
unsupported Anthropic and Fireworks cache settings from each fallback attempt,
while preserving settings accepted by the selected fallback.

This provider knowledge lives here because an outer caching middleware never
re-runs during fallback and therefore cannot clean up after itself.

## Properties

- `ResponseT`
- `logger`

## Methods

- [`init_chat_model()`](https://reference.langchain.com/python/langchain/agents/middleware/model_fallback/init_chat_model)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/be854a130153e51346d83d3b06f959b80f6cbca6/libs/langchain_v1/langchain/agents/middleware/model_fallback.py)
