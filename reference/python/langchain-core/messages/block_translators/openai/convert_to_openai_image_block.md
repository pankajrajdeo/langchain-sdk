---
title: "convert_to_openai_image_block"
description: "Convert ImageContentBlock to format expected by OpenAI Chat Completions."
source: "https://reference.langchain.com/python/langchain-core/messages/block_translators/openai/convert_to_openai_image_block"
category: "reference"
tags: [reference, langchain-core, messages, block_translators, openai, convert_to_openai_image_block]
---

# convert_to_openai_image_block

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/block_translators/openai/convert_to_openai_image_block)

Convert `ImageContentBlock` to format expected by OpenAI Chat Completions.

## Signature

```python
convert_to_openai_image_block(
    block: dict[str, Any],
) -> dict[str, Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `block` | `dict[str, Any]` | Yes | The image content block to convert. |

## Returns

`dict[str, Any]`

The formatted image content block.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/messages/block_translators/openai.py#L22)
