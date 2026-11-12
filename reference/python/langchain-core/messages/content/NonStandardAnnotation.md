---
title: "NonStandardAnnotation"
description: "Provider-specific annotation format."
source: "https://reference.langchain.com/python/langchain-core/messages/content/NonStandardAnnotation"
category: "reference"
tags: [reference, langchain-core, messages, content, nonstandardannotation]
---

# NonStandardAnnotation

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/NonStandardAnnotation)

Provider-specific annotation format.

## Signature

```python
NonStandardAnnotation()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['non_standard_annotation'],
    id: NotRequired[str],
    value: dict[str, Any],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['non_standard_annotation']` |
| `id` | `NotRequired[str]` |
| `value` | `dict[str, Any]` |

## Properties

- `type`
- `id`
- `value`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/messages/content.py#L184)
