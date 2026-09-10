---
title: "ImageURL"
description: "Image URL for multimodal model inputs (OpenAI format)."
source: "https://reference.langchain.com/python/langchain-core/prompt_values/ImageURL"
category: "reference"
tags: [reference, langchain-core, prompt_values, imageurl]
---

# ImageURL

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompt_values/ImageURL)

Image URL for multimodal model inputs (OpenAI format).

Represents the inner `image_url` object in OpenAI's Chat Completion API format. This
is used by `ImagePromptTemplate` and `ChatPromptTemplate`.

## Signature

```python
ImageURL()
```

## Description

**See Also:**

`ImageContentBlock`: LangChain's provider-agnostic image format used in message
content blocks. Use `ImageContentBlock` when working with the standardized
message format across different providers.

**Note:**

The `detail` field values are not validated locally. Invalid values
will be rejected by the downstream API, allowing new valid values to
be used without requiring a LangChain update.

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    detail: Literal['auto', 'low', 'high'],
    url: str,
)
```

| Name | Type |
|------|------|
| `detail` | `Literal['auto', 'low', 'high']` |
| `url` | `str` |

## Properties

- `detail`
- `url`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/prompt_values.py#L107)
