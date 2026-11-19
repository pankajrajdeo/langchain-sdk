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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/2b7ff14fb2021e6f4ee22f796a9b888eaacb5af9/libs/core/langchain_core/decisions/types.py#L324)
