---
title: "StreamPartV2"
description: "Type Alias in langgraph_sdk"
source: "https://reference.langchain.com/python/langgraph-sdk/schema/StreamPartV2"
category: "reference"
tags: [reference, langgraph-sdk, schema, streampartv2]
---

# StreamPartV2

> **Type Alias** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/StreamPartV2)

Discriminated union of all v2 stream part types.

Use `part["type"]` to narrow the type.

## Signature

```python
StreamPartV2 = ValuesStreamPart | UpdatesStreamPart | MessagesPartialStreamPart | MessagesCompleteStreamPart | MessagesMetadataStreamPart | MessagesTupleStreamPart | CustomStreamPart | CheckpointsStreamPart | TasksStreamPart | DebugStreamPart | MetadataStreamPart
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/6b83b9b019c9b2680e4456dd6835d0fea27b9887/libs/sdk-py/langgraph_sdk/schema.py#L858)
