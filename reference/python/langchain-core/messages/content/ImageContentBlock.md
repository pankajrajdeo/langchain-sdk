---
title: "ImageContentBlock"
description: "Image data."
source: "https://reference.langchain.com/python/langchain-core/messages/content/ImageContentBlock"
category: "reference"
tags: [reference, langchain-core, messages, content, imagecontentblock]
---

# ImageContentBlock

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/ImageContentBlock)

Image data.

!!! note "Factory function"

    `create_image_block` may also be used as a factory to create an
    `ImageContentBlock`. Benefits include:

    * Automatic ID generation (when not provided)
    * Required arguments strictly validated at creation time

## Signature

```python
ImageContentBlock()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['image'],
    id: NotRequired[str],
    file_id: NotRequired[str],
    mime_type: NotRequired[str],
    index: NotRequired[int | str],
    url: NotRequired[str],
    base64: NotRequired[str],
    extras: NotRequired[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['image']` |
| `id` | `NotRequired[str]` |
| `file_id` | `NotRequired[str]` |
| `mime_type` | `NotRequired[str]` |
| `index` | `NotRequired[int \| str]` |
| `url` | `NotRequired[str]` |
| `base64` | `NotRequired[str]` |
| `extras` | `NotRequired[dict[str, Any]]` |

## Properties

- `type`
- `id`
- `file_id`
- `mime_type`
- `index`
- `url`
- `base64`
- `extras`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/messages/content.py#L498)
