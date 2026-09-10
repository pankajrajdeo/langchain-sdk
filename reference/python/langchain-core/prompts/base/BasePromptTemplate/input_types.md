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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/prompts/base.py#L55)
