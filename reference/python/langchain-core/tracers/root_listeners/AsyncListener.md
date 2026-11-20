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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d4dafe5839c4a6b07d71cc78697df0de9e627e21/libs/core/langchain_core/tracers/root_listeners.py#L18)
