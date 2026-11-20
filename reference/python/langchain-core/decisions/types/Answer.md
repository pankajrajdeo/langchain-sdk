---
title: "Answer"
description: "A discriminated union of answers returned by decision models."
source: "https://reference.langchain.com/python/langchain-core/decisions/types/Answer"
category: "reference"
tags: [reference, langchain-core, decisions, types, answer]
---

# Answer

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/decisions/types/Answer)

A discriminated union of answers returned by decision models.

## Signature

```python
Answer = Annotated[NoulAnswer | ChoiceAnswer | ScoreAnswer | BoxAnswer, Field(discriminator='type')]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d4dafe5839c4a6b07d71cc78697df0de9e627e21/libs/core/langchain_core/decisions/types.py#L328)
