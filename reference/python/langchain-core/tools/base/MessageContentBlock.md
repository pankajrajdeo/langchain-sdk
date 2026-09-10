---
title: "MessageContentBlock"
description: "Type Alias in langchain_core"
source: "https://reference.langchain.com/python/langchain-core/tools/base/MessageContentBlock"
category: "reference"
tags: [reference, langchain-core, tools, base, messagecontentblock]
---

# MessageContentBlock

> **Type Alias** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/base/MessageContentBlock)

A single message content block: plain text or a structured block.

A dict block is only considered valid at runtime when its `type` key is one of
`TOOL_MESSAGE_BLOCK_TYPES` (see `_is_message_content_block`); the static type
intentionally stays broad because block payloads vary by provider format.

## Signature

```python
MessageContentBlock = str | dict[str, Any]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/tools/base.py#L382)
