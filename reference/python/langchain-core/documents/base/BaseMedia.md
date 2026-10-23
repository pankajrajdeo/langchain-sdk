---
title: "BaseMedia"
description: "Base class for content used in retrieval and data processing workflows."
source: "https://reference.langchain.com/python/langchain-core/documents/base/BaseMedia"
category: "reference"
tags: [reference, langchain-core, documents, base, basemedia]
---

# BaseMedia

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/documents/base/BaseMedia)

Base class for content used in retrieval and data processing workflows.

Provides common fields for content that needs to be stored, indexed, or searched.

!!! note

    For multimodal content in **chat messages** (images, audio sent to/from LLMs),
    use `langchain.messages` content blocks instead.

## Signature

```python
BaseMedia(
    self,
    args: Any = (),
    kwargs: Any = {},
)
```

## Extends

- `Serializable`

## Properties

- `id`
- `metadata`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/documents/base.py#L34)
