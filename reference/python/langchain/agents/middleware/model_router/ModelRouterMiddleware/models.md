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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ced9bdb1a8899516b6c541fc0e19ab5f349aa0ea/libs/langchain_v1/langchain/agents/middleware/model_router.py#L132)
