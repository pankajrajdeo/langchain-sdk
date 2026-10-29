---
title: "cache"
description: "Whether to cache the response."
source: "https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/cache"
category: "reference"
tags: [reference, langchain-core, language_models, base, baselanguagemodel, cache]
---

# cache

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/cache)

Whether to cache the response.

* If `True`, will use the global cache.
* If `False`, will not use a cache
* If `None`, will use the global cache if it's set, otherwise no cache.
* If instance of `BaseCache`, will use the provided cache.

Caching is not currently supported for streaming methods of models.

## Signature

```python
cache: BaseCache | bool | None = Field(default=None, exclude=True)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/6419339aa163a49f32d9b80ff20d6adc3b446d49/libs/core/langchain_core/language_models/base.py#L190)
