---
title: "translate_content"
description: "Derive standard content blocks from a message with Anthropic content."
source: "https://reference.langchain.com/python/langchain-core/messages/block_translators/anthropic/translate_content"
category: "reference"
tags: [reference, langchain-core, messages, block_translators, anthropic, translate_content]
---

# translate_content

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/block_translators/anthropic/translate_content)

Derive standard content blocks from a message with Anthropic content.

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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/2b7ff14fb2021e6f4ee22f796a9b888eaacb5af9/libs/core/langchain_core/messages/block_translators/anthropic.py#L537)
