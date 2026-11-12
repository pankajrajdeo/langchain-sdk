---
title: "input_types"
description: "A dictionary of the types of the variables the prompt template expects."
source: "https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/input_types"
category: "reference"
tags: [reference, langchain-core, prompts, base, baseprompttemplate, input_types]
---

# input_types

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/input_types)

A dictionary of the types of the variables the prompt template expects.

If not provided, all variables are assumed to be strings.

## Signature

```python
input_types: builtins.dict[str, Any] = Field(default_factory=dict, exclude=True)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/prompts/base.py#L55)
