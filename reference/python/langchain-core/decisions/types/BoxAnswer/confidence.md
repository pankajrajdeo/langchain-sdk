---
title: "confidence"
description: "Certainty from 0 to 1, or None when the provider does not report it."
source: "https://reference.langchain.com/python/langchain-core/decisions/types/BoxAnswer/confidence"
category: "reference"
tags: [reference, langchain-core, decisions, types, boxanswer, confidence]
---

# confidence

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/decisions/types/BoxAnswer/confidence)

Certainty from `0` to `1`, or `None` when the provider does not report it.

## Signature

```python
confidence: float | None = Field(default=None, ge=0.0, le=1.0)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d4dafe5839c4a6b07d71cc78697df0de9e627e21/libs/core/langchain_core/decisions/types.py#L324)
