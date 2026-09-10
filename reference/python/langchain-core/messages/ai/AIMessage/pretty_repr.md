---
title: "pretty_repr"
description: "Return a pretty representation of the message for display."
source: "https://reference.langchain.com/python/langchain-core/messages/ai/AIMessage/pretty_repr"
category: "reference"
tags: [reference, langchain-core, messages, ai, aimessage, pretty_repr]
---

# pretty_repr

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/ai/AIMessage/pretty_repr)

Return a pretty representation of the message for display.

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
from langchain_core.messages import AIMessage

msg = AIMessage(
    content="Let me check the weather.",
    tool_calls=[
        {"name": "get_weather", "args": {"city": "Paris"}, "id": "1"}
    ],
)
```

Results in:
```python
>>> print(msg.pretty_repr())
================================== Ai Message ==================================

Let me check the weather.
Tool Calls:
  get_weather (1)
 Call ID: 1
  Args:
    city: Paris
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `html` | `bool` | No | Whether to return an HTML-formatted string. (default: `False`) |

## Returns

`str`

A pretty representation of the message.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/messages/ai.py#L353)
