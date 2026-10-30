---
title: "get_child"
description: "Get a child callback manager."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/ParentRunManager/get_child"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, parentrunmanager, get_child]
---

# get_child

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/ParentRunManager/get_child)

Get a child callback manager.

## Signature

```python
get_child(
    self,
    tag: str | None = None,
) -> CallbackManager
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `tag` | `str \| None` | No | The tag for the child callback manager. (default: `None`) |

## Returns

`CallbackManager`

The child callback manager.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/callbacks/manager.py#L613)
