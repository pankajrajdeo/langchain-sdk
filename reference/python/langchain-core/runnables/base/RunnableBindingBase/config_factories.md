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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/runnables/base.py#L5880)
