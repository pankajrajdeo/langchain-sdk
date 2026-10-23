---
title: "aadd"
description: "Asynchronously add a sequence of addable objects together."
source: "https://reference.langchain.com/python/langchain-core/runnables/utils/aadd"
category: "reference"
tags: [reference, langchain-core, runnables, utils, aadd]
---

# aadd

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/aadd)

Asynchronously add a sequence of addable objects together.

## Signature

```python
aadd(
    addables: AsyncIterable[Addable],
) -> Addable | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `addables` | `AsyncIterable[Addable]` | Yes | The addable objects to add. |

## Returns

`Addable | None`

The result of adding the addable objects.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/runnables/utils.py#L561)
