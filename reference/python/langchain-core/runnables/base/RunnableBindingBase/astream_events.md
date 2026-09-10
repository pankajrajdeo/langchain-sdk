---
title: "astream_events"
description: "Forward astream_events to the bound runnable with bound kwargs merged."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/astream_events"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnablebindingbase, astream_events]
---

# astream_events

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/astream_events)

Forward `astream_events` to the bound runnable with bound kwargs merged.

For `version="v3"`, returns an awaitable that resolves to the
bound runnable's typed stream object (e.g. `AsyncChatModelStream`).
For `version="v1"` / `"v2"`, returns an async iterator over
`StreamEvent` items.

Without this override, `__getattr__` would drop `self.kwargs` — losing
tools bound via `bind_tools`, `stop` sequences, etc.

## Signature

```python
astream_events(
    self,
    input: Input,
    config: RunnableConfig | None = None,
    **kwargs: Any | None = {},
) -> AsyncIterator[StreamEvent] | Awaitable[Any]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/base.py#L6314)
