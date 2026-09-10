---
title: "on_stream_event"
description: "Run on each protocol event from astream_events(version=\"v3\")."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForLLMRun/on_stream_event"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, asynccallbackmanagerforllmrun, on_stream_event]
---

# on_stream_event

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForLLMRun/on_stream_event)

Run on each protocol event from `astream_events(version="v3")`.

## Signature

```python
on_stream_event(
    self,
    event: MessagesData,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `event` | `MessagesData` | Yes | The protocol event. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/callbacks/manager.py#L907)
