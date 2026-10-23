---
title: "get_child"
description: "Get a child callback manager."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncParentRunManager/get_child"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, asyncparentrunmanager, get_child]
---

# get_child

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncParentRunManager/get_child)

Get a child callback manager.

## Signature

```python
get_child(
    self,
    tag: str | None = None,
) -> AsyncCallbackManager
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `tag` | `str \| None` | No | The tag for the child callback manager. (default: `None`) |

## Returns

`AsyncCallbackManager`

The child callback manager.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/callbacks/manager.py#L697)
