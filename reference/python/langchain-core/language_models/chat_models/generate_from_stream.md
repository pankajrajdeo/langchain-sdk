---
title: "generate_from_stream"
description: "Generate from a stream."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_models/generate_from_stream"
category: "reference"
tags: [reference, langchain-core, language_models, chat_models, generate_from_stream]
---

# generate_from_stream

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/chat_models/generate_from_stream)

Generate from a stream.

## Signature

```python
generate_from_stream(
    stream: Iterator[ChatGenerationChunk],
) -> ChatResult
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `stream` | `Iterator[ChatGenerationChunk]` | Yes | Iterator of `ChatGenerationChunk`. |

## Returns

`ChatResult`

Chat result.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/language_models/chat_models.py#L218)
