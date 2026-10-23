---
title: "bind_pump"
description: "Bind a pump for standalone streaming."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/ChatModelStream/bind_pump"
category: "reference"
tags: [reference, langchain-core, language_models, chat_model_stream, chatmodelstream, bind_pump]
---

# bind_pump

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/ChatModelStream/bind_pump)

Bind a pump for standalone streaming.

Delegates to `set_request_more`.  Used by
`BaseChatModel.stream_events(version="v3")`.

## Signature

```python
bind_pump(
    self,
    pump_one: Callable[[], bool],
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/bdf0f53ed0aec3c9ae371a549e1a4d2ee4e9f021/libs/core/langchain_core/language_models/chat_model_stream.py#L1243)
