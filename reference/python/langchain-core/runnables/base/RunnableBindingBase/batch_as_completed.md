---
title: "batch_as_completed"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/batch_as_completed"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnablebindingbase, batch_as_completed]
---

# batch_as_completed

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/batch_as_completed)

## Signature

```python
batch_as_completed(
    self,
    inputs: Sequence[Input],
    config: RunnableConfig | Sequence[RunnableConfig] | None = None,
    *,
    return_exceptions: bool = False,
    **kwargs: Any | None = {},
) -> Iterator[tuple[int, Output | Exception]]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/base.py#L6099)
