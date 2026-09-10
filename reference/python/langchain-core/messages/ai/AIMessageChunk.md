---
title: "AIMessageChunk"
description: "Message chunk from an AI (yielded when streaming)."
source: "https://reference.langchain.com/python/langchain-core/messages/ai/AIMessageChunk"
category: "reference"
tags: [reference, langchain-core, messages, ai, aimessagechunk]
---

# AIMessageChunk

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/ai/AIMessageChunk)

Message chunk from an AI (yielded when streaming).

## Signature

```python
AIMessageChunk(
    self,
    content: str | list[str | dict[Any, Any]] | None = None,
    content_blocks: list[types.ContentBlock] | None = None,
    **kwargs: Any = {},
)
```

## Extends

- `AIMessage`
- `BaseMessageChunk`

## Properties

- `type`
- `tool_call_chunks`
- `chunk_position`
- `lc_attributes`
- `content_blocks`

## Methods

- [`init_tool_calls()`](https://reference.langchain.com/python/langchain-core/messages/ai/AIMessageChunk/init_tool_calls)
- [`init_server_tool_calls()`](https://reference.langchain.com/python/langchain-core/messages/ai/AIMessageChunk/init_server_tool_calls)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/messages/ai.py#L418)
