---
title: "recast_checkpoint_ns"
description: "Remove task IDs from checkpoint namespace."
source: "https://reference.langchain.com/python/langgraph/_internal/_config/recast_checkpoint_ns"
category: "reference"
tags: [reference, langgraph, internal, config, recast_checkpoint_ns]
---

# recast_checkpoint_ns

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_config/recast_checkpoint_ns)

Remove task IDs from checkpoint namespace.

## Signature

```python
recast_checkpoint_ns(
    ns: str,
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `ns` | `str` | Yes | The checkpoint namespace with task IDs. |

## Returns

`str`

The checkpoint namespace without task IDs.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/_internal/_config.py#L50)
