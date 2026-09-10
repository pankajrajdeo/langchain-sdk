---
title: "abatch_as_completed"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/abatch_as_completed"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnablebindingbase, abatch_as_completed]
---

# abatch_as_completed

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/abatch_as_completed)

## Signature

```python
abatch_as_completed(
    self,
    inputs: Sequence[Input],
    config: RunnableConfig | Sequence[RunnableConfig] | None = None,
    *,
    return_exceptions: bool = False,
    **kwargs: Any | None = {},
) -> AsyncIterator[tuple[int, Output | Exception]]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/base.py#L6151)
