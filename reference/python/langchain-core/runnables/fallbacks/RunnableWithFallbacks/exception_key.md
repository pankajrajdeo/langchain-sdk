---
title: "exception_key"
description: "If string is specified then handled exceptions will be passed to fallbacks as part of the input under the specified key."
source: "https://reference.langchain.com/python/langchain-core/runnables/fallbacks/RunnableWithFallbacks/exception_key"
category: "reference"
tags: [reference, langchain-core, runnables, fallbacks, runnablewithfallbacks, exception_key]
---

# exception_key

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/fallbacks/RunnableWithFallbacks/exception_key)

If `string` is specified then handled exceptions will be passed to fallbacks as
part of the input under the specified key.

If `None`, exceptions will not be passed to fallbacks.

If used, the base `Runnable` and its fallbacks must accept a dictionary as input.

## Signature

```python
exception_key: str | None = None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/fallbacks.py#L98)
