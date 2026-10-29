---
title: "set_start"
description: "Install a lazy-start callback on this stream and its projections."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/AsyncChatModelStream/set_start"
category: "reference"
tags: [reference, langchain-core, language_models, chat_model_stream, asyncchatmodelstream, set_start]
---

# set_start

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/AsyncChatModelStream/set_start)

Install a lazy-start callback on this stream and its projections.

## Signature

```python
set_start(
    self,
    cb: Callable[[], Awaitable[None]] | None,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/6419339aa163a49f32d9b80ff20d6adc3b446d49/libs/core/langchain_core/language_models/chat_model_stream.py#L1421)
