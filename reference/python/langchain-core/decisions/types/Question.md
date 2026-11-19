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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/2b7ff14fb2021e6f4ee22f796a9b888eaacb5af9/libs/core/langchain_core/decisions/types.py#L224)
