---
title: "batch"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/language_models/llms/BaseLLM/batch"
category: "reference"
tags: [reference, langchain-core, language_models, llms, basellm, batch]
---

# batch

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/llms/BaseLLM/batch)

## Signature

```python
batch(
    self,
    inputs: list[LanguageModelInput],
    config: RunnableConfig | list[RunnableConfig] | None = None,
    *,
    return_exceptions: bool = False,
    **kwargs: Any = {},
) -> list[str]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/language_models/llms.py#L420)
