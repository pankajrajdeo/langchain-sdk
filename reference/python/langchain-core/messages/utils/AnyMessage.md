---
title: "AnyMessage"
description: "A type representing any defined Message or MessageChunk type."
source: "https://reference.langchain.com/python/langchain-core/messages/utils/AnyMessage"
category: "reference"
tags: [reference, langchain-core, messages, utils, anymessage]
---

# AnyMessage

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/utils/AnyMessage)

A type representing any defined `Message` or `MessageChunk` type.

## Signature

```python
AnyMessage = Annotated[Annotated[AIMessage, Tag(tag='ai')] | Annotated[HumanMessage, Tag(tag='human')] | Annotated[ChatMessage, Tag(tag='chat')] | Annotated[SystemMessage, Tag(tag='system')] | Annotated[FunctionMessage, Tag(tag='function')] | Annotated[ToolMessage, Tag(tag='tool')] | Annotated[AIMessageChunk, Tag(tag='AIMessageChunk')] | Annotated[HumanMessageChunk, Tag(tag='HumanMessageChunk')] | Annotated[ChatMessageChunk, Tag(tag='ChatMessageChunk')] | Annotated[SystemMessageChunk, Tag(tag='SystemMessageChunk')] | Annotated[FunctionMessageChunk, Tag(tag='FunctionMessageChunk')] | Annotated[ToolMessageChunk, Tag(tag='ToolMessageChunk')], Field(discriminator=Discriminator(_get_type))]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/messages/utils.py#L86)
