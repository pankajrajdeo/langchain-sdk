---
title: "NoulCriteria"
description: "Optional descriptions for the two outcomes of a Noul question."
source: "https://reference.langchain.com/python/langchain-core/decisions/types/NoulCriteria"
category: "reference"
tags: [reference, langchain-core, decisions, types, noulcriteria]
---

# NoulCriteria

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/decisions/types/NoulCriteria)

Optional descriptions for the two outcomes of a `Noul` question.

Criteria clarify what should count as yes and no when the instruction alone leaves
room for interpretation. Both values accept any JSON-compatible content, so callers
can provide a short description or structured examples.

## Signature

```python
NoulCriteria()
```

## Extends

- `BaseModel`

## Properties

- `model_config`
- `true`
- `false`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d4dafe5839c4a6b07d71cc78697df0de9e627e21/libs/core/langchain_core/decisions/types.py#L43)
