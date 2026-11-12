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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/decisions/types.py#L224)
