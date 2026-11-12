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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/messages/base.py#L134)
