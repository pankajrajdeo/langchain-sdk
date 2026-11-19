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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/2b7ff14fb2021e6f4ee22f796a9b888eaacb5af9/libs/core/langchain_core/decisions/types.py#L43)
