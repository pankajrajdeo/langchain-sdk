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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d4dafe5839c4a6b07d71cc78697df0de9e627e21/libs/core/langchain_core/decisions/types.py#L268)
