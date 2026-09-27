---
title: "translate_content_chunk"
description: "Derive standard content blocks from a message chunk with Anthropic content."
source: "https://reference.langchain.com/python/langchain-core/messages/block_translators/anthropic/translate_content_chunk"
category: "reference"
tags: [reference, langchain-core, messages, block_translators, anthropic, translate_content_chunk]
---

# translate_content_chunk

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/block_translators/anthropic/translate_content_chunk)

Derive standard content blocks from a message chunk with Anthropic content.

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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/messages/block_translators/anthropic.py#L510)
