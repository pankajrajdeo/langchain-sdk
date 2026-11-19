---
title: "ContextFraction"
description: "Fraction of model's maximum input tokens."
source: "https://reference.langchain.com/python/langchain/agents/middleware/summarization/ContextFraction"
category: "reference"
tags: [reference, langchain, agents, middleware, summarization, contextfraction]
---

# ContextFraction

> **Attribute** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/summarization/ContextFraction)

Fraction of model's maximum input tokens.

## Signature

```python
ContextFraction = tuple[Literal['fraction'], float]
```

## Description

**Example:**

To specify 50% of the model's max input tokens:

```python
("fraction", 0.5)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ced9bdb1a8899516b6c541fc0e19ab5f349aa0ea/libs/langchain_v1/langchain/agents/middleware/summarization.py#L156)
