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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/decisions/types.py#L228)
