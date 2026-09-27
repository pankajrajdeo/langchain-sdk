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
    **kwargs: Any = {},
) -> AsyncIterator[AIMessageChunk]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/language_models/chat_models.py#L857)
