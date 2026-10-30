---
title: "translate_content"
description: "Derive standard content blocks from a message with OpenAI content."
source: "https://reference.langchain.com/python/langchain-core/messages/block_translators/openai/translate_content"
category: "reference"
tags: [reference, langchain-core, messages, block_translators, openai, translate_content]
---

# translate_content

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/block_translators/openai/translate_content)

Derive standard content blocks from a message with OpenAI content.

## Signature

```python
translate_content(
    message: AIMessage,
) -> list[types.ContentBlock]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `message` | `AIMessage` | Yes | The message to translate. |

## Returns

`list[types.ContentBlock]`

The derived content blocks.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/messages/block_translators/openai.py#L1047)
