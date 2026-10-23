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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/bdf0f53ed0aec3c9ae371a549e1a4d2ee4e9f021/libs/core/langchain_core/messages/base.py#L106)
