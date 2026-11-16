---
title: "optional_variables"
description: "A list of the names of the variables for placeholder or MessagePlaceholder that are optional."
source: "https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/optional_variables"
category: "reference"
tags: [reference, langchain-core, prompts, base, baseprompttemplate, optional_variables]
---

# optional_variables

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/optional_variables)

A list of the names of the variables for placeholder or `MessagePlaceholder` that
are optional.

These variables are auto inferred from the prompt and user need not provide them.

## Signature

```python
optional_variables: list[str] = Field(default=[])
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ea17e48f0a4336c920394fd029de99f1568b4c38/libs/core/langchain_core/prompts/base.py#L48)
