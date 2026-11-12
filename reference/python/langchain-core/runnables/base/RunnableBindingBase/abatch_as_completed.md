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
    kwargs: Any | None = {},
) -> AsyncIterator[tuple[int, Output | Exception]]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/runnables/base.py#L6138)
