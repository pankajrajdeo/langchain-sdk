---
title: "write_to"
description: "Add channel writes."
source: "https://reference.langchain.com/python/langgraph/pregel/main/NodeBuilder/write_to"
category: "reference"
tags: [reference, langgraph, pregel, main, nodebuilder, write_to]
---

# write_to

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/main/NodeBuilder/write_to)

Add channel writes.

## Signature

```python
write_to(
    self,
    channels: str | ChannelWriteEntry = (),
    kwargs: _WriteValue = {},
) -> Self
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `*channels` | `str \| ChannelWriteEntry` | No | Channel names to write to. (default: `()`) |
| `**kwargs` | `_WriteValue` | No | Channel name and value mappings. (default: `{}`) |

## Returns

`Self`

Self for chaining

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/pregel/main.py#L323)
