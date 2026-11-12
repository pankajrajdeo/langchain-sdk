---
title: "process"
description: "Drop tagged messages events after nudging MessagesTransformer to ignore them."
source: "https://reference.langchain.com/python/langchain/agents/middleware/internal_call_transformer/InternalCallTransformer/process"
category: "reference"
tags: [reference, langchain, agents, middleware, internal_call_transformer, internalcalltransformer, process]
---

# process

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/internal_call_transformer/InternalCallTransformer/process)

Drop tagged `messages` events after nudging `MessagesTransformer` to ignore them.

## Signature

```python
process(
    self,
    event: ProtocolEvent,
) -> bool
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `event` | `ProtocolEvent` | Yes | The protocol event to observe, and possibly mutate. |

## Returns

`bool`

`False` to drop a tagged internal call from the raw event log and

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c2f4036e4c6ca45a8da8a42d8e07a25d2ea48b8f/libs/langchain_v1/langchain/agents/middleware/internal_call_transformer.py#L76)
