---
title: "AsyncListener"
description: "Type Alias in langchain_core"
source: "https://reference.langchain.com/python/langchain-core/tracers/root_listeners/AsyncListener"
category: "reference"
tags: [reference, langchain-core, tracers, root_listeners, asynclistener]
---

# AsyncListener

> **Type Alias** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/root_listeners/AsyncListener)

## Signature

```python
AsyncListener = Callable[[Run], Awaitable[None]] | Callable[[Run, RunnableConfig], Awaitable[None]]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/tracers/root_listeners.py#L18)
