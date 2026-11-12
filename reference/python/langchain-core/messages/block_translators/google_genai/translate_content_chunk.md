---
title: "translate_content_chunk"
description: "Derive standard content blocks from a chunk with Google (GenAI) content."
source: "https://reference.langchain.com/python/langchain-core/messages/block_translators/google_genai/translate_content_chunk"
category: "reference"
tags: [reference, langchain-core, messages, block_translators, google_genai, translate_content_chunk]
---

# translate_content_chunk

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/block_translators/google_genai/translate_content_chunk)

Derive standard content blocks from a chunk with Google (GenAI) content.

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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/messages/block_translators/google_genai.py#L623)
