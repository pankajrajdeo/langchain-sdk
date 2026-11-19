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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/2b7ff14fb2021e6f4ee22f796a9b888eaacb5af9/libs/core/langchain_core/runnables/base.py#L5851)
