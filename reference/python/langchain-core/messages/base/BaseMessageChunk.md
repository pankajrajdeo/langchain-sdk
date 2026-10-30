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
    kwargs: Any = {},
)
```

## Extends

- `BaseMessage`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/messages/base.py#L412)
