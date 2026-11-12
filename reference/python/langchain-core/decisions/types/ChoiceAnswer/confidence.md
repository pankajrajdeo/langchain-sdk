---
title: "confidence"
description: "Scalar certainty from 0 to 1 in the selected label."
source: "https://reference.langchain.com/python/langchain-core/decisions/types/ChoiceAnswer/confidence"
category: "reference"
tags: [reference, langchain-core, decisions, types, choiceanswer, confidence]
---

# confidence

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/decisions/types/ChoiceAnswer/confidence)

Scalar certainty from `0` to `1` in the selected label.

Each provider documents how it derives confidence. Thresholds should be chosen
according to the consequences of an incorrect automated decision.

## Signature

```python
confidence: float = Field(ge=0.0, le=1.0)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/decisions/types.py#L268)
