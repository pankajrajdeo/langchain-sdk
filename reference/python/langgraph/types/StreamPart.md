---
title: "StreamPart"
description: "A discriminated union of all v2 stream part types."
source: "https://reference.langchain.com/python/langgraph/types/StreamPart"
category: "reference"
tags: [reference, langgraph, types, streampart]
---

# StreamPart

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/StreamPart)

A discriminated union of all v2 stream part types.

Use `part["type"]` to narrow the type:

```python
async for part in graph.astream(input, version="v2"):
    if part["type"] == "values":
        part["data"]  # OutputT — full state (pydantic/dataclass/dict)
    elif part["type"] == "messages":
        part["data"]  # tuple[BaseMessage, dict] — (message, metadata)
    elif part["type"] == "custom":
        part["data"]  # Any — user-defined
```

## Signature

```python
StreamPart = TypeAliasType('StreamPart', ValuesStreamPart[OutputT] | UpdatesStreamPart | MessagesStreamPart | CustomStreamPart | CheckpointStreamPart[StateT] | TasksStreamPart | DebugStreamPart[StateT], type_params=(StateT, OutputT))
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93/libs/langgraph/langgraph/types.py#L353)
