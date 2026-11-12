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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/messages/base.py#L105)
