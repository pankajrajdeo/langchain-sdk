---
title: "BaseMessageChunk"
description: "Message chunk, which can be concatenated with other Message chunks."
source: "https://reference.langchain.com/python/langchain-core/messages/base/BaseMessageChunk"
category: "reference"
tags: [reference, langchain-core, messages, base, basemessagechunk]
---

# BaseMessageChunk

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/base/BaseMessageChunk)

Message chunk, which can be concatenated with other Message chunks.

## Signature

```python
BaseMessageChunk(
    self,
    content: str | list[str | dict[Any, Any]] | None = None,
    content_blocks: list[types.ContentBlock] | None = None,
    **kwargs: Any = {},
)
```

## Extends

- `BaseMessage`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/messages/base.py#L409)
