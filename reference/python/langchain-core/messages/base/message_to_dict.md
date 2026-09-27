---
title: "message_to_dict"
description: "Convert a Message to a dictionary."
source: "https://reference.langchain.com/python/langchain-core/messages/base/message_to_dict"
category: "reference"
tags: [reference, langchain-core, messages, base, message_to_dict]
---

# message_to_dict

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/base/message_to_dict)

Convert a Message to a dictionary.

## Signature

```python
message_to_dict(
    message: BaseMessage,
) -> dict[str, Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `message` | `BaseMessage` | Yes | Message to convert. |

## Returns

`dict[str, Any]`

Message as a dict. The dict will have a `type` key with the message type

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/messages/base.py#L474)
