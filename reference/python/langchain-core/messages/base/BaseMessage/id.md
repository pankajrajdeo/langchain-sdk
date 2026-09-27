---
title: "id"
description: "An optional unique identifier for the message."
source: "https://reference.langchain.com/python/langchain-core/messages/base/BaseMessage/id"
category: "reference"
tags: [reference, langchain-core, messages, base, basemessage, id]
---

# id

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/base/BaseMessage/id)

An optional unique identifier for the message.

This should ideally be provided by the provider/model which created the message.

## Signature

```python
id: str | None = Field(default=None, coerce_numbers_to_str=True)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/messages/base.py#L135)
