---
title: "translate_content_chunk"
description: "Derive standard content blocks from a chunk with Google (GenAI) content."
source: "https://reference.langchain.com/python/langchain-core/messages/block_translators/google_vertexai/translate_content_chunk"
category: "reference"
tags: [reference, langchain-core, messages, block_translators, google_vertexai, translate_content_chunk]
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/messages/block_translators/google_genai.py#L586)
