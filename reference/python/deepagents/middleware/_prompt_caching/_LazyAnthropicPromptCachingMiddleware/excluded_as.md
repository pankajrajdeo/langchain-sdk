---
title: "excluded_as"
description: "Return the class that a class-form excluded_middleware entry must name to drop this middleware."
source: "https://reference.langchain.com/python/deepagents/middleware/_prompt_caching/_LazyAnthropicPromptCachingMiddleware/excluded_as"
category: "reference"
tags: [reference, deepagents, middleware, prompt_caching, lazyanthropicpromptcachingmiddleware, excluded_as]
---

# excluded_as

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/_prompt_caching/_LazyAnthropicPromptCachingMiddleware/excluded_as)

Return the class that a class-form `excluded_middleware` entry must name to drop this middleware.

A caller that names `AnthropicPromptCachingMiddleware` has imported it,
so a `sys.modules` lookup finds it without importing.

## Signature

```python
excluded_as: type[AgentMiddleware[Any, Any, Any]]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/middleware/_prompt_caching.py#L47)
