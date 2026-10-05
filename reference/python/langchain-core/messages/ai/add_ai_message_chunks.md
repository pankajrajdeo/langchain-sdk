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
    *others: AIMessageChunk = (),
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/04ac76c07ec173a44e3e57de54861d0b637e3299/libs/core/langchain_core/messages/ai.py#L651)
