---
title: "from_template"
description: "Create a chat prompt template from a template string."
source: "https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/from_template"
category: "reference"
tags: [reference, langchain-core, prompts, chat, chatprompttemplate, from_template]
---

# from_template

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/from_template)

Create a chat prompt template from a template string.

Creates a chat template consisting of a single message assumed to be from the
human.

## Signature

```python
from_template(
    cls,
    template: str,
    **kwargs: Any = {},
) -> ChatPromptTemplate
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `template` | `str` | Yes | Template string |
| `**kwargs` | `Any` | No | Keyword arguments to pass to the constructor. (default: `{}`) |

## Returns

`ChatPromptTemplate`

A new instance of this class.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/prompts/chat.py#L1105)
