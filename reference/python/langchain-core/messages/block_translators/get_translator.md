---
title: "get_translator"
description: "Get the translator functions for a provider."
source: "https://reference.langchain.com/python/langchain-core/messages/block_translators/get_translator"
category: "reference"
tags: [reference, langchain-core, messages, block_translators, get_translator]
---

# get_translator

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/block_translators/get_translator)

Get the translator functions for a provider.

## Signature

```python
get_translator(
    provider: str,
) -> dict[str, Callable[..., list[types.ContentBlock]]] | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `provider` | `str` | Yes | The model provider name. |

## Returns

`dict[str, Callable[..., list[types.ContentBlock]]] | None`

Dictionary with `'translate_content'` and `'translate_content_chunk'`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/messages/block_translators/__init__.py#L57)
