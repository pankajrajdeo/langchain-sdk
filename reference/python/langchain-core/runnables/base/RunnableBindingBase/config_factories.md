---
title: "config_factories"
description: "The config factories to bind to the underlying Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/config_factories"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnablebindingbase, config_factories]
---

# config_factories

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/config_factories)

The config factories to bind to the underlying `Runnable`.

## Signature

```python
config_factories: list[Callable[[RunnableConfig], RunnableConfig]] = Field(default_factory=list)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/runnables/base.py#L5863)
