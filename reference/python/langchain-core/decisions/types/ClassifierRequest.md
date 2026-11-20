---
title: "ClassifierRequest"
description: "Complete input for one decision model invocation."
source: "https://reference.langchain.com/python/langchain-core/decisions/types/ClassifierRequest"
category: "reference"
tags: [reference, langchain-core, decisions, types, classifierrequest]
---

# ClassifierRequest

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/decisions/types/ClassifierRequest)

Complete input for one decision model invocation.

Keeping the state and questions in the Runnable input ensures both values
participate in composition, batching, and tracing.

## Signature

```python
ClassifierRequest()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    state: State,
    questions: Mapping[str, Question],
)
```

| Name | Type |
|------|------|
| `state` | `State` |
| `questions` | `Mapping[str, Question]` |

## Properties

- `state`
- `questions`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d4dafe5839c4a6b07d71cc78697df0de9e627e21/libs/core/langchain_core/decisions/types.py#L228)
