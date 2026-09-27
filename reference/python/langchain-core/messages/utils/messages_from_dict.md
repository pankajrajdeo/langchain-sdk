---
title: "messages_from_dict"
description: "Convert a sequence of messages from dicts to Message objects."
source: "https://reference.langchain.com/python/langchain-core/messages/utils/messages_from_dict"
category: "reference"
tags: [reference, langchain-core, messages, utils, messages_from_dict]
---

# messages_from_dict

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/utils/messages_from_dict)

Convert a sequence of messages from dicts to `Message` objects.

## Signature

```python
messages_from_dict(
    messages: Sequence[dict[str, Any]],
) -> list[BaseMessage]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `messages` | `Sequence[dict[str, Any]]` | Yes | Sequence of messages (as dicts) to convert. |

## Returns

`list[BaseMessage]`

list of messages (BaseMessages).

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/messages/utils.py#L560)
