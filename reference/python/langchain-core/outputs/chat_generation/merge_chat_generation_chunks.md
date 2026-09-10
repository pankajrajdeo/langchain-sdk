---
title: "merge_chat_generation_chunks"
description: "Merge a list of ChatGenerationChunks into a single ChatGenerationChunk."
source: "https://reference.langchain.com/python/langchain-core/outputs/chat_generation/merge_chat_generation_chunks"
category: "reference"
tags: [reference, langchain-core, outputs, chat_generation, merge_chat_generation_chunks]
---

# merge_chat_generation_chunks

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/outputs/chat_generation/merge_chat_generation_chunks)

Merge a list of `ChatGenerationChunk`s into a single `ChatGenerationChunk`.

## Signature

```python
merge_chat_generation_chunks(
    chunks: list[ChatGenerationChunk],
) -> ChatGenerationChunk | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `chunks` | `list[ChatGenerationChunk]` | Yes | A list of `ChatGenerationChunk` to merge. |

## Returns

`ChatGenerationChunk | None`

A merged `ChatGenerationChunk`, or `None` if the input list is empty.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/outputs/chat_generation.py#L140)
