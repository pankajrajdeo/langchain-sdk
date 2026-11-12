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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/decisions/types.py#L328)
