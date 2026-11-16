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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ea17e48f0a4336c920394fd029de99f1568b4c38/libs/core/langchain_core/runnables/utils.py#L546)
