---
title: "pretty_repr"
description: "Get a pretty representation of the message."
source: "https://reference.langchain.com/python/langchain-core/messages/base/BaseMessage/pretty_repr"
category: "reference"
tags: [reference, langchain-core, messages, base, basemessage, pretty_repr]
---

# pretty_repr

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/base/BaseMessage/pretty_repr)

Get a pretty representation of the message.

## Signature

```python
pretty_repr(
    self,
    html: bool = False,
) -> str
```

## Description

**Example:**

```python
from langchain_core.messages import HumanMessage

msg = HumanMessage(content="What is the capital of France?")
print(msg.pretty_repr())
```

Results in:

```txt
================================ Human Message =================================

What is the capital of France?
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `html` | `bool` | No | Whether to format the message as HTML. If `True`, the message will be formatted with HTML tags. (default: `False`) |

## Returns

`str`

A pretty representation of the message.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/messages/base.py#L309)
