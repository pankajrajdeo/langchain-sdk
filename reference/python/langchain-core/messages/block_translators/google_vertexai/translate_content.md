---
title: "translate_content"
description: "Derive standard content blocks from a message with Google (GenAI) content."
source: "https://reference.langchain.com/python/langchain-core/messages/block_translators/google_vertexai/translate_content"
category: "reference"
tags: [reference, langchain-core, messages, block_translators, google_vertexai, translate_content]
---

# translate_content

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/block_translators/google_genai/translate_content)

Derive standard content blocks from a message with Google (GenAI) content.

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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/04ac76c07ec173a44e3e57de54861d0b637e3299/libs/core/langchain_core/messages/block_translators/google_genai.py#L574)
