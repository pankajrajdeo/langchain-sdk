---
title: "batch"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/runnables/configurable/DynamicRunnable/batch"
category: "reference"
tags: [reference, langchain-core, runnables, configurable, dynamicrunnable, batch]
---

# batch

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/configurable/DynamicRunnable/batch)

## Signature

```python
batch(
    self,
    inputs: list[Input],
    config: RunnableConfig | list[RunnableConfig] | None = None,
    *,
    return_exceptions: bool = False,
    **kwargs: Any | None = {},
) -> list[Output]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/configurable.py#L154)
