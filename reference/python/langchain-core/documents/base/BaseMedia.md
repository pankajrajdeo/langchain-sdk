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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/documents/base.py#L34)
