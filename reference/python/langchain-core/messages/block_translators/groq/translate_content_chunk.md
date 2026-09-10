---
title: "translate_content_chunk"
description: "Derive standard content blocks from a message chunk with groq content."
source: "https://reference.langchain.com/python/langchain-core/messages/block_translators/groq/translate_content_chunk"
category: "reference"
tags: [reference, langchain-core, messages, block_translators, groq, translate_content_chunk]
---

# translate_content_chunk

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/block_translators/groq/translate_content_chunk)

Derive standard content blocks from a message chunk with groq content.

## Signature

```python
translate_content_chunk(
    message: AIMessageChunk,
) -> list[types.ContentBlock]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `message` | `AIMessageChunk` | Yes | The message chunk to translate. |

## Returns

`list[types.ContentBlock]`

The derived content blocks.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/messages/block_translators/groq.py#L133)
