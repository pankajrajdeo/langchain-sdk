---
title: "astream"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/language_models/llms/BaseLLM/astream"
category: "reference"
tags: [reference, langchain-core, language_models, llms, basellm, astream]
---

# astream

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/llms/BaseLLM/astream)

## Signature

```python
astream(
    self,
    input: LanguageModelInput,
    config: RunnableConfig | None = None,
    *,
    stop: list[str] | None = None,
    kwargs: Any = {},
) -> AsyncIterator[str]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/language_models/llms.py#L583)
