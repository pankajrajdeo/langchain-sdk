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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/middleware/summarization.py#L125)
