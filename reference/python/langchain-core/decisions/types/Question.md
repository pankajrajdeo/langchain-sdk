---
title: "Question"
description: "A discriminated union of question types accepted by decision models."
source: "https://reference.langchain.com/python/langchain-core/decisions/types/Question"
category: "reference"
tags: [reference, langchain-core, decisions, types, question]
---

# Question

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/decisions/types/Question)

A discriminated union of question types accepted by decision models.

## Signature

```python
Question = Annotated[Noul | Choice | Score | Box, Field(discriminator='type')]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/5069b326c53069ec85a7e1d914c6873feb8d0cfa/libs/core/langchain_core/decisions/types.py#L224)
