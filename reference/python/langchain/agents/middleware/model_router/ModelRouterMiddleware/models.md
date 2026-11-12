---
title: "models"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain/agents/middleware/model_router/ModelRouterMiddleware/models"
category: "reference"
tags: [reference, langchain, agents, middleware, model_router, modelroutermiddleware, models]
---

# models

> **Attribute** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/model_router/ModelRouterMiddleware/models)

## Signature

```python
models = {route: init_chat_model(choice.model) if isinstance(choice.model, str) else choice.model for route, choice in self.config.choices.items()}
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c2f4036e4c6ca45a8da8a42d8e07a25d2ea48b8f/libs/langchain_v1/langchain/agents/middleware/model_router.py#L132)
