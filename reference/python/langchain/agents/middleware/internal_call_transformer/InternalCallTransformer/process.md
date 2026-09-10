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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/middleware/internal_call_transformer.py#L76)
