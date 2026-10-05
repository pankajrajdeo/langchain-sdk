---
title: "exceptions_to_handle"
description: "The exceptions on which fallbacks should be tried."
source: "https://reference.langchain.com/python/langchain-core/runnables/fallbacks/RunnableWithFallbacks/exceptions_to_handle"
category: "reference"
tags: [reference, langchain-core, runnables, fallbacks, runnablewithfallbacks, exceptions_to_handle]
---

# exceptions_to_handle

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/fallbacks/RunnableWithFallbacks/exceptions_to_handle)

The exceptions on which fallbacks should be tried.

Any exception that is not a subclass of these exceptions will be raised immediately.

## Signature

```python
exceptions_to_handle: tuple[type[BaseException], ...] = (Exception,)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/04ac76c07ec173a44e3e57de54861d0b637e3299/libs/core/langchain_core/runnables/fallbacks.py#L93)
