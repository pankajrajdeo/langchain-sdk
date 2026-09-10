---
title: "optional"
description: "Whether format_messages must be provided."
source: "https://reference.langchain.com/python/langchain-core/prompts/chat/MessagesPlaceholder/optional"
category: "reference"
tags: [reference, langchain-core, prompts, chat, messagesplaceholder, optional]
---

# optional

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/chat/MessagesPlaceholder/optional)

Whether `format_messages` must be provided.

If `True` `format_messages` can be called with no arguments and will return an empty
list.

If `False` then a named argument with name `variable_name` must be passed in, even
if the value is an empty list.

## Signature

```python
optional: bool = False
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/prompts/chat.py#L129)
