---
title: "agenerate_from_stream"
description: "Async generate from a stream."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_models/agenerate_from_stream"
category: "reference"
tags: [reference, langchain-core, language_models, chat_models, agenerate_from_stream]
---

# agenerate_from_stream

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/chat_models/agenerate_from_stream)

Async generate from a stream.

## Signature

```python
agenerate_from_stream(
    stream: AsyncIterator[ChatGenerationChunk],
) -> ChatResult
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `stream` | `AsyncIterator[ChatGenerationChunk]` | Yes | AsyncIterator of `ChatGenerationChunk`. |

## Returns

`ChatResult`

Chat result.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/e936943647fe9bd9c4c24122ee3e1812ead82130/libs/core/langchain_core/language_models/chat_models.py#L288)
