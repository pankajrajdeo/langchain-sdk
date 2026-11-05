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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/b4aa7e7d00c452251720ce30b8bc2c41ca44e1f5/libs/core/langchain_core/tracers/root_listeners.py#L18)
