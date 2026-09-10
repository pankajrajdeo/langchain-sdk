---
title: "partial"
description: "Get a new ChatPromptTemplate with some input variables already filled in."
source: "https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/partial"
category: "reference"
tags: [reference, langchain-core, prompts, chat, chatprompttemplate, partial]
---

# partial

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/partial)

Get a new `ChatPromptTemplate` with some input variables already filled in.

## Signature

```python
partial(
    self,
    **kwargs: Any = {},
) -> ChatPromptTemplate
```

## Description

**Example:**

```python
from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an AI assistant named {name}."),
        ("human", "Hi I'm {user}"),
        ("ai", "Hi there, {user}, I'm {name}."),
        ("human", "{input}"),
    ]
)
template2 = template.partial(user="Lucy", name="R2D2")

template2.format_messages(input="hello")
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `**kwargs` | `Any` | No | Keyword arguments to use for filling in template variables.  Ought to be a subset of the input variables. (default: `{}`) |

## Returns

`ChatPromptTemplate`

A new `ChatPromptTemplate`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/prompts/chat.py#L1230)
