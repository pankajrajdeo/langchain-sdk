---
title: "messages_to_dict"
description: "Convert a sequence of Messages to a list of dictionaries."
source: "https://reference.langchain.com/python/langchain-core/messages/messages_to_dict"
category: "reference"
tags: [reference, langchain-core, messages, messages_to_dict]
---

# messages_to_dict

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/base/messages_to_dict)

Convert a sequence of Messages to a list of dictionaries.

## Signature

```python
messages_to_dict(
    messages: Sequence[BaseMessage],
) -> list[dict[str, Any]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `messages` | `Sequence[BaseMessage]` | Yes | Sequence of messages (as `BaseMessage`s) to convert. |

## Returns

`list[dict[str, Any]]`

List of messages as dicts.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/messages/base.py#L488)
