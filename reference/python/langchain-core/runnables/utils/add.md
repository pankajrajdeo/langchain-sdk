---
title: "add"
description: "Add a sequence of addable objects together."
source: "https://reference.langchain.com/python/langchain-core/runnables/utils/add"
category: "reference"
tags: [reference, langchain-core, runnables, utils, add]
---

# add

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/add)

Add a sequence of addable objects together.

## Signature

```python
add(
    addables: Iterable[Addable],
) -> Addable | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `addables` | `Iterable[Addable]` | Yes | The addable objects to add. |

## Returns

`Addable | None`

The result of adding the addable objects.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/runnables/utils.py#L546)
