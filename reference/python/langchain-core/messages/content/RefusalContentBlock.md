---
title: "RefusalContentBlock"
description: "An explicit refusal reported by the model provider."
source: "https://reference.langchain.com/python/langchain-core/messages/content/RefusalContentBlock"
category: "reference"
tags: [reference, langchain-core, messages, content, refusalcontentblock]
---

# RefusalContentBlock

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/RefusalContentBlock)

An explicit refusal reported by the model provider.

Providers report refusals differently: OpenAI returns refusal content, while
Anthropic reports a refusal stop reason on the response. Both are represented
as this block so callers can detect a refusal without provider-specific code.
Refusals the model writes as ordinary text are not detected.

!!! version-added "Added in `langchain-core` 1.7.5"

## Signature

```python
RefusalContentBlock()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['refusal'],
    refusal: str,
    id: NotRequired[str],
    index: NotRequired[int | str],
    extras: NotRequired[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['refusal']` |
| `refusal` | `str` |
| `id` | `NotRequired[str]` |
| `index` | `NotRequired[int \| str]` |
| `extras` | `NotRequired[dict[str, Any]]` |

## Properties

- `type`
- `refusal`
- `id`
- `index`
- `extras`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/messages/content.py#L495)
