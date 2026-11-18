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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/5069b326c53069ec85a7e1d914c6873feb8d0cfa/libs/core/langchain_core/decisions/types.py#L261)
