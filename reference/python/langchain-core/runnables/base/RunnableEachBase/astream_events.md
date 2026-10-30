---
title: "astream_events"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableEachBase/astream_events"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnableeachbase, astream_events]
---

# astream_events

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableEachBase/astream_events)

## Signature

```python
astream_events(
    self,
    input: Input,
    config: RunnableConfig | None = None,
    *,
    version: Literal['v1', 'v2', 'v3'] = 'v2',
    kwargs: Any | None = {},
) -> AsyncIterator[StreamEvent] | Awaitable[Any]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/runnables/base.py#L5714)
