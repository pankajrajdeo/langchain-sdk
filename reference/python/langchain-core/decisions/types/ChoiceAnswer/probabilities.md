---
title: "probabilities"
description: "Probability assigned to each candidate label, keyed by label name."
source: "https://reference.langchain.com/python/langchain-core/decisions/types/ChoiceAnswer/probabilities"
category: "reference"
tags: [reference, langchain-core, decisions, types, choiceanswer, probabilities]
---

# probabilities

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/decisions/types/ChoiceAnswer/probabilities)

Probability assigned to each candidate label, keyed by label name.

The complete distribution is retained so applications can use a confidence measure
or risk policy different from the provider's.

## Signature

```python
probabilities: dict[str, float]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d4dafe5839c4a6b07d71cc78697df0de9e627e21/libs/core/langchain_core/decisions/types.py#L261)
