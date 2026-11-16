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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ea17e48f0a4336c920394fd029de99f1568b4c38/libs/core/langchain_core/decisions/types.py#L224)
