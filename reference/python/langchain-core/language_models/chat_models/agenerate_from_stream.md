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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/language_models/chat_models.py#L247)
