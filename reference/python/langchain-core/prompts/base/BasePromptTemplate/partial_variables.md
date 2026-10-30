---
title: "partial_variables"
description: "A dictionary of the partial variables the prompt template carries."
source: "https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/partial_variables"
category: "reference"
tags: [reference, langchain-core, prompts, base, baseprompttemplate, partial_variables]
---

# partial_variables

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/partial_variables)

A dictionary of the partial variables the prompt template carries.

Partial variables populate the template so that you don't need to pass them in every
time you call the prompt.

## Signature

```python
partial_variables: Mapping[str, Any] = Field(default_factory=dict)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/prompts/base.py#L67)
