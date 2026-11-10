---
title: "additional_kwargs"
description: "Reserved for additional payload data associated with the message."
source: "https://reference.langchain.com/python/langchain-core/messages/base/BaseMessage/additional_kwargs"
category: "reference"
tags: [reference, langchain-core, messages, base, basemessage, additional_kwargs]
---

# additional_kwargs

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/base/BaseMessage/additional_kwargs)

Reserved for additional payload data associated with the message.

For example, for a message from an AI, this could include tool calls as
encoded by the model provider.

## Signature

```python
additional_kwargs: dict[Any, Any] = Field(default_factory=dict)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/1a41b51b0295d7cc6df45cdede199b4a34649b1d/libs/core/langchain_core/messages/base.py#L106)
