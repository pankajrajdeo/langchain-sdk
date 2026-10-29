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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/6419339aa163a49f32d9b80ff20d6adc3b446d49/libs/core/langchain_core/messages/block_translators/groq.py#L133)
