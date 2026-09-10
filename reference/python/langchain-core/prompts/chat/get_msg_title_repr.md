---
title: "get_msg_title_repr"
description: "Get a title representation for a message."
source: "https://reference.langchain.com/python/langchain-core/prompts/chat/get_msg_title_repr"
category: "reference"
tags: [reference, langchain-core, prompts, chat, get_msg_title_repr]
---

# get_msg_title_repr

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/base/get_msg_title_repr)

Get a title representation for a message.

## Signature

```python
get_msg_title_repr(
    title: str,
    *,
    bold: bool = False,
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `title` | `str` | Yes | The title. |
| `bold` | `bool` | No | Whether to bold the title. (default: `False`) |

## Returns

`str`

The title representation.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/messages/base.py#L501)
