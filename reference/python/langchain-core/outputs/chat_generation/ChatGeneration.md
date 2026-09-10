---
title: "ChatGeneration"
description: "A single chat generation output."
source: "https://reference.langchain.com/python/langchain-core/outputs/chat_generation/ChatGeneration"
category: "reference"
tags: [reference, langchain-core, outputs, chat_generation, chatgeneration]
---

# ChatGeneration

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/outputs/chat_generation/ChatGeneration)

A single chat generation output.

A subclass of `Generation` that represents the response from a chat model that
generates chat messages.

The `message` attribute is a structured representation of the chat message. Most of
the time, the message will be of type `AIMessage`.

Users working with chat models will usually access information via either
`AIMessage` (returned from runnable interfaces) or `LLMResult` (available via
callbacks).

## Signature

```python
ChatGeneration(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `Generation`

## Properties

- `text`
- `message`
- `type`

## Methods

- [`set_text()`](https://reference.langchain.com/python/langchain-core/outputs/chat_generation/ChatGeneration/set_text)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/outputs/chat_generation.py#L17)
