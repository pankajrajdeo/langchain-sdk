---
title: "ClassifierResponse"
description: "Typed answers and metadata returned from one classification request."
source: "https://reference.langchain.com/python/langchain-core/decisions/types/ClassifierResponse"
category: "reference"
tags: [reference, langchain-core, decisions, types, classifierresponse]
---

# ClassifierResponse

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/decisions/types/ClassifierResponse)

Typed answers and metadata returned from one classification request.

Access every answer through `answers`, or use `nouls`, `choices`, `scores`, and
`boxes` for views filtered by answer type. Each mapping preserves the question IDs
supplied to `ClassifierRequest.questions`.

## Signature

```python
ClassifierResponse()
```

## Extends

- `BaseModel`

## Properties

- `model`
- `answers`
- `usage`
- `request_id`
- `nouls`
- `choices`
- `scores`
- `boxes`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/5069b326c53069ec85a7e1d914c6873feb8d0cfa/libs/core/langchain_core/decisions/types.py#L335)
