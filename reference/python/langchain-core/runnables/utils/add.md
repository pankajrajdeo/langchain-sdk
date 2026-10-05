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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/04ac76c07ec173a44e3e57de54861d0b637e3299/libs/core/langchain_core/runnables/utils.py#L545)
