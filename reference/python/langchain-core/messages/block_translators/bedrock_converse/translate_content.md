---
title: "translate_content"
description: "Derive standard content blocks from a message with Bedrock Converse content."
source: "https://reference.langchain.com/python/langchain-core/messages/block_translators/bedrock_converse/translate_content"
category: "reference"
tags: [reference, langchain-core, messages, block_translators, bedrock_converse, translate_content]
---

# translate_content

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/block_translators/bedrock_converse/translate_content)

Derive standard content blocks from a message with Bedrock Converse content.

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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/5069b326c53069ec85a7e1d914c6873feb8d0cfa/libs/core/langchain_core/messages/block_translators/bedrock_converse.py#L297)
