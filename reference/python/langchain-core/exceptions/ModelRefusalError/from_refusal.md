---
title: "from_refusal"
description: "Create a ModelRefusalError from a standard refusal block."
source: "https://reference.langchain.com/python/langchain-core/exceptions/ModelRefusalError/from_refusal"
category: "reference"
tags: [reference, langchain-core, exceptions, modelrefusalerror, from_refusal]
---

# from_refusal

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/exceptions/ModelRefusalError/from_refusal)

Create a `ModelRefusalError` from a standard refusal block.

## Signature

```python
from_refusal(
    cls,
    refusal: RefusalContentBlock,
    *,
    raw_message: BaseMessage,
) -> ModelRefusalError
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `refusal` | `RefusalContentBlock` | Yes | The refusal block from the response's `content_blocks`. |
| `raw_message` | `BaseMessage` | Yes | The model response that contained the refusal. |

## Returns

`ModelRefusalError`

An error whose message includes the refusal's category and text.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/exceptions.py#L169)
