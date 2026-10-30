---
title: "add_ai_message_chunks"
description: "Add multiple AIMessageChunks together."
source: "https://reference.langchain.com/python/langchain-core/messages/ai/add_ai_message_chunks"
category: "reference"
tags: [reference, langchain-core, messages, ai, add_ai_message_chunks]
---

# add_ai_message_chunks

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/ai/add_ai_message_chunks)

Add multiple `AIMessageChunk`s together.

## Signature

```python
add_ai_message_chunks(
    left: AIMessageChunk,
    others: AIMessageChunk = (),
) -> AIMessageChunk
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `left` | `AIMessageChunk` | Yes | The first `AIMessageChunk`. |
| `*others` | `AIMessageChunk` | No | Other `AIMessageChunk`s to add. (default: `()`) |

## Returns

`AIMessageChunk`

The resulting `AIMessageChunk`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/messages/ai.py#L651)
