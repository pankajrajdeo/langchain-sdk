---
title: "translate_content_chunk"
description: "Derive standard content blocks from a chunk with Bedrock Converse content."
source: "https://reference.langchain.com/python/langchain-core/messages/block_translators/bedrock_converse/translate_content_chunk"
category: "reference"
tags: [reference, langchain-core, messages, block_translators, bedrock_converse, translate_content_chunk]
---

# translate_content_chunk

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/block_translators/bedrock_converse/translate_content_chunk)

Derive standard content blocks from a chunk with Bedrock Converse content.

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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/messages/block_translators/bedrock_converse.py#L309)
