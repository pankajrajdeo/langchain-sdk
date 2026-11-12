---
title: "kwargs"
description: "kwargs to pass to the underlying Runnable when running."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/kwargs"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnablebindingbase, kwargs]
---

# kwargs

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/kwargs)

kwargs to pass to the underlying `Runnable` when running.

For example, when the `Runnable` binding is invoked the underlying
`Runnable` will be invoked with the same input but with these additional
kwargs.

## Signature

```python
kwargs: Mapping[str, Any] = Field(default_factory=dict)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/runnables/base.py#L5851)
