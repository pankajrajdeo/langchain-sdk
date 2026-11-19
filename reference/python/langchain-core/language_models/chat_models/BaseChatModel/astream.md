---
title: "astream"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/astream"
category: "reference"
tags: [reference, langchain-core, language_models, chat_models, basechatmodel, astream]
---

# astream

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/astream)

## Signature

```python
astream(
    self,
    input: LanguageModelInput,
    config: RunnableConfig | None = None,
    *,
    stop: list[str] | None = None,
    kwargs: Any = {},
) -> AsyncIterator[AIMessageChunk]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/2b7ff14fb2021e6f4ee22f796a9b888eaacb5af9/libs/core/langchain_core/language_models/chat_models.py#L900)
