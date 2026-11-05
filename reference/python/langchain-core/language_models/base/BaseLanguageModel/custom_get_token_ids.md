---
title: "custom_get_token_ids"
description: "Optional encoder to use for counting tokens."
source: "https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/custom_get_token_ids"
category: "reference"
tags: [reference, langchain-core, language_models, base, baselanguagemodel, custom_get_token_ids]
---

# custom_get_token_ids

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/custom_get_token_ids)

Optional encoder to use for counting tokens.

## Signature

```python
custom_get_token_ids: Callable[[str], list[int]] | None = Field(default=None, exclude=True)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/b4aa7e7d00c452251720ce30b8bc2c41ca44e1f5/libs/core/langchain_core/language_models/base.py#L213)
