---
title: "astream_events"
description: "Async variant of stream_events. See stream_events for full docs."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/astream_events"
category: "reference"
tags: [reference, langchain-core, language_models, chat_models, basechatmodel, astream_events]
---

# astream_events

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/astream_events)

Async variant of `stream_events`. See `stream_events` for full docs.

## Signature

```python
astream_events(
    self,
    input: LanguageModelInput,
    config: RunnableConfig | None = None,
    *,
    version: Literal['v1', 'v2', 'v3'] = 'v2',
    stop: list[str] | None = None,
    kwargs: Any = {},
) -> AsyncIterator[StreamEvent] | Awaitable[AsyncChatModelStream]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/b4aa7e7d00c452251720ce30b8bc2c41ca44e1f5/libs/core/langchain_core/language_models/chat_models.py#L1424)
