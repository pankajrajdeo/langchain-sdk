---
title: "translate_content"
description: "Derive standard content blocks from a message with Bedrock content."
source: "https://reference.langchain.com/python/langchain-core/messages/block_translators/bedrock/translate_content"
category: "reference"
tags: [reference, langchain-core, messages, block_translators, bedrock, translate_content]
---

# translate_content

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/block_translators/bedrock/translate_content)

Derive standard content blocks from a message with Bedrock content.

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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/b4aa7e7d00c452251720ce30b8bc2c41ca44e1f5/libs/core/langchain_core/messages/block_translators/bedrock.py#L67)
