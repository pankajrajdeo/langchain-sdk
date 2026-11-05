---
title: "chunk_position"
description: "Optional span represented by an aggregated AIMessageChunk."
source: "https://reference.langchain.com/python/langchain-core/messages/ai/AIMessageChunk/chunk_position"
category: "reference"
tags: [reference, langchain-core, messages, ai, aimessagechunk, chunk_position]
---

# chunk_position

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/ai/AIMessageChunk/chunk_position)

Optional span represented by an aggregated `AIMessageChunk`.

If a chunk with `chunk_position="last"` is aggregated into a stream,
`tool_call_chunks` in message content will be parsed into `tool_calls`.

## Signature

```python
chunk_position: Literal['last'] | None = None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/b4aa7e7d00c452251720ce30b8bc2c41ca44e1f5/libs/core/langchain_core/messages/ai.py#L430)
