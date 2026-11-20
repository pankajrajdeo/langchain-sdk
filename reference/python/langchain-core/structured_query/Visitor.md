---
title: "Visitor"
description: "Defines interface for IR translation using a visitor pattern."
source: "https://reference.langchain.com/python/langchain-core/structured_query/Visitor"
category: "reference"
tags: [reference, langchain-core, structured_query, visitor]
---

# Visitor

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/structured_query/Visitor)

Defines interface for IR translation using a visitor pattern.

## Signature

```python
Visitor()
```

## Extends

- `ABC`

## Properties

- `allowed_comparators`
- `allowed_operators`

## Methods

- [`visit_operation()`](https://reference.langchain.com/python/langchain-core/structured_query/Visitor/visit_operation)
- [`visit_comparison()`](https://reference.langchain.com/python/langchain-core/structured_query/Visitor/visit_comparison)
- [`visit_structured_query()`](https://reference.langchain.com/python/langchain-core/structured_query/Visitor/visit_structured_query)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d4dafe5839c4a6b07d71cc78697df0de9e627e21/libs/core/langchain_core/structured_query.py#L15)
