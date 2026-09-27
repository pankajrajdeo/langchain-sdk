---
title: "set_request_more"
description: "Install the pull callback the iterator uses to drain the source."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/SyncProjection/set_request_more"
category: "reference"
tags: [reference, langchain-core, language_models, chat_model_stream, syncprojection, set_request_more]
---

# set_request_more

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/SyncProjection/set_request_more)

Install the pull callback the iterator uses to drain the source.

## Signature

```python
set_request_more(
    self,
    cb: Callable[[], bool] | None,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/language_models/chat_model_stream.py#L242)
