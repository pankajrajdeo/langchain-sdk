---
title: "register_translator"
description: "Register content translators for a provider in PROVIDER_TRANSLATORS."
source: "https://reference.langchain.com/python/langchain-core/messages/block_translators/register_translator"
category: "reference"
tags: [reference, langchain-core, messages, block_translators, register_translator]
---

# register_translator

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/block_translators/register_translator)

Register content translators for a provider in `PROVIDER_TRANSLATORS`.

## Signature

```python
register_translator(
    provider: str,
    translate_content: Callable[[AIMessage], list[types.ContentBlock]],
    translate_content_chunk: Callable[[AIMessageChunk], list[types.ContentBlock]],
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `provider` | `str` | Yes | The model provider name (e.g. `'openai'`, `'anthropic'`). |
| `translate_content` | `Callable[[AIMessage], list[types.ContentBlock]]` | Yes | Function to translate `AIMessage` content. |
| `translate_content_chunk` | `Callable[[AIMessageChunk], list[types.ContentBlock]]` | Yes | Function to translate `AIMessageChunk` content. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/messages/block_translators/__init__.py#L39)
