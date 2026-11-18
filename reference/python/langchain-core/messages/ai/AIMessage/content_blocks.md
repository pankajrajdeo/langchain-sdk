---
title: "content_blocks"
description: "Return standard, typed ContentBlock dicts from the message."
source: "https://reference.langchain.com/python/langchain-core/messages/ai/AIMessage/content_blocks"
category: "reference"
tags: [reference, langchain-core, messages, ai, aimessage, content_blocks]
---

# content_blocks

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/ai/AIMessage/content_blocks)

Return standard, typed `ContentBlock` dicts from the message.

If the message has a known model provider, use the provider-specific translator
first before falling back to best-effort parsing. For details, see the property
on `BaseMessage`.

## Signature

```python
content_blocks: list[types.ContentBlock]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/5069b326c53069ec85a7e1d914c6873feb8d0cfa/libs/core/langchain_core/messages/ai.py#L243)
