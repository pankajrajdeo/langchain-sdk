---
title: "block_translators"
description: "Derivations of standard content blocks from provider content."
source: "https://reference.langchain.com/python/langchain-core/messages/block_translators"
category: "reference"
tags: [reference, langchain-core, messages, block_translators]
---

# block_translators

> **Module** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/block_translators)

Derivations of standard content blocks from provider content.

`AIMessage` will first attempt to use a provider-specific translator if
`model_provider` is set in `response_metadata` on the message. Consequently, each
provider translator must handle all possible content response types from the provider,
including text.

If no provider is set, or if the provider does not have a registered translator,
`AIMessage` will fall back to best-effort parsing of the content into blocks using
the implementation in `BaseMessage`.

## Properties

- `PROVIDER_TRANSLATORS`

## Methods

- [`register_translator()`](https://reference.langchain.com/python/langchain-core/messages/block_translators/register_translator)
- [`get_translator()`](https://reference.langchain.com/python/langchain-core/messages/block_translators/get_translator)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/messages/block_translators/__init__.py)
